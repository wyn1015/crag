from typing import Dict, List, Any
import os
import torch
from PIL import Image
from agents.base_agent import BaseAgent
from cragmm_search.search import UnifiedSearchPipeline
import vllm
import json
from .domain.domain_class import DomainClassifier
import re
import logging

# 配置常量
AICROWD_SUBMISSION_BATCH_SIZE = 64
VLLM_TENSOR_PARALLEL_SIZE = 1
VLLM_GPU_MEMORY_UTILIZATION = 0.70
MAX_MODEL_LEN = 8192
MAX_NUM_SEQS = 2
MAX_GENERATION_TOKENS = 75
NUM_SEARCH_RESULTS = 3
INITIAL_SEARCH_RESULTS = 10  # Initial number of search results to fetch

# 从 agents.template 导入 DOMAIN_PROMPTS
from agents.template import DOMAIN_PROMPTS

class SimpleRAGAgent6domainranker3imagetwo1352model4(BaseAgent):
    """
    改进后的RAG Agent，移除了文本搜索和重排模块
    只使用图像搜索功能
    """
    
    def __init__(
        self, 
        search_pipeline: UnifiedSearchPipeline, 
        model_name: str = "illusionnnnnnn/team-aicrowd-my-model5", 
        max_gen_len: int = 64
    ):
        super().__init__(search_pipeline)
        logging.info("初始化 RAG Agent...")
        if search_pipeline is None:
            raise ValueError("Search pipeline is required for RAG agent")
        
        try:
            print(f"[DEBUG] 加载 DomainClassifier...")
            self.domain_classifier = DomainClassifier("zoeeee12/team-aicrowd-my-model3")
            print(f"[DEBUG] DomainClassifier 加载成功")
        except Exception as e:
            print(f"[ERROR] DomainClassifier 加载失败: {str(e)}")
            raise
            
        self.model_name = model_name
        self.max_gen_len = max_gen_len
        self.initialize_models()

    def initialize_models(self):
        """初始化LLM和tokenizer"""
        print(f"Initializing {self.model_name} with vLLM...")
        
        self.llm = vllm.LLM(
            self.model_name,
            tensor_parallel_size=VLLM_TENSOR_PARALLEL_SIZE,
            gpu_memory_utilization=VLLM_GPU_MEMORY_UTILIZATION,
            max_model_len=MAX_MODEL_LEN,
            max_num_seqs=MAX_NUM_SEQS,
            trust_remote_code=True,
            dtype="bfloat16",
            enforce_eager=True,
            limit_mm_per_prompt={"image": 1}
        )
        self.tokenizer = self.llm.get_tokenizer()

    def get_batch_size(self) -> int:
        return AICROWD_SUBMISSION_BATCH_SIZE

    def get_image_search_results(self, image: Image.Image, k: int = 2):
        """获取图像搜索结果并进行过滤"""
        results = self.search_pipeline(image, k=k*2)
        print(f"[DEBUG] 原始图像搜索结果: {results}")
        
        valid_results = [r for r in results if r.get('score', 0) > 0.6 and len(r.get('entities', [])) > 0]
        print(f"[DEBUG] 过滤后图像结果数: {len(valid_results)}")
        
        return valid_results[:k] if valid_results else []

    def prepare_rag_context(self, search_results: List[Dict]) -> str:
        """格式化搜索结果上下文（过滤无效属性）"""
        if not search_results:
            return ""
            
        context = []
        for i, res in enumerate(search_results, 1):
            source_type = "Image"
            confidence = res.get('score', 0)
            url = res.get('url') or res.get('page_url', 'N/A')
            name = res.get('page_name', 'Unnamed Result')

            result_block = [
                f"[Result {i}] Type: {source_type}",
                f"Confidence: {confidence:.2f}",
                f"URL: {url}",
                f"Title: {name}"
            ]

            if entities := res.get('entities'):
                entity_info = []
                for ent in entities:
                    cleaned_ent = self.remove_nulls_and_placeholders(ent)
                    ent_name = cleaned_ent.get('entity_name', 'Unnamed Entity')
                    attrs = cleaned_ent.get('entity_attributes', {})
                    
                    # 过滤无效属性
                    valid_attrs = {
                        k: v for k, v in attrs.items()
                        if v not in (None, "<>", "", "null")
                        and not (isinstance(v, str) and v.strip() == "")
                    }
                    
                    attr_lines = []
                    for attr, val in valid_attrs.items():
                        if isinstance(val, str):
                            val = self.clean_content_v3(val)
                            if attr == 'description':
                                val = val[:1000] + "..." if len(val) > 1000 else val
                        attr_lines.append(f"    • {attr}: {val}")

                    if attr_lines:
                        entity_info.append(
                            f"  Entity: {ent_name}\n" + 
                            "\n".join(attr_lines)
                        )
                    else:
                        entity_info.append(f"  Entity: {ent_name} (No valid attributes)")

                if entity_info:
                    result_block.append("\nDetected Entities:\n" + "\n\n".join(entity_info))

            if snippet := res.get('page_snippet'):
                clean_snippet = self.clean_content_v3(snippet.replace('\n', ' ').strip())
                result_block.append(f"Content: {clean_snippet}...")

            context.append("\n".join(result_block))

        return (
            "\n\n# SEARCH CONTEXT #\n\n" +
            "\n\n".join(context) + 
            "\n\n"
        )
   
    def prepare_initial_inputs(
        self, 
        queries: List[str], 
        images: List[Image.Image],
        message_histories: List[List[Dict[str, Any]]]
    ) -> List[dict]:
        """准备第一阶段生成输入（生成搜索查询）"""
        inputs = []
        domain_counter = {}
        
        for query, image, history in zip(queries, images, message_histories):
            try:
                domain_id = self.domain_classifier.predict(query)
                print(f"预测的 domain_id: {domain_id}")
                
                if domain_id not in DOMAIN_PROMPTS:
                    raise KeyError(f"domain_id {domain_id} 不存在于 DOMAIN_PROMPTS 中")
                
                domain_prompt = DOMAIN_PROMPTS[domain_id]
                print(f"使用的 prompt: {domain_prompt[:50]}...")
                
            except Exception as e:
                print(f"[ERROR] 分类失败: {str(e)}")
                domain_id = -1
                domain_prompt = DOMAIN_PROMPTS[-1]
            
            domain_counter[domain_id] = domain_counter.get(domain_id, 0) + 1
            
            messages = []
            if history:
                messages.extend(history)
            messages.append({
                "role": "user",
                "content": [
                    {"type": "image"},
                    {"type": "text", "text": f"{domain_prompt} Entities may involve multiple fields. Please generate search keywords and sentences based on the questions raised by the entities in the figure. Query: {query}"}
                ]
            })
          
            formatted_prompt = self.tokenizer.apply_chat_template(
                messages,
                add_generation_prompt=True,
                tokenize=False
            )
            text_tokens = len(self.tokenizer.encode(formatted_prompt, add_special_tokens=False))
            used_percent = text_tokens / MAX_MODEL_LEN * 100
            status = "⚠️ OVERLIMIT" if text_tokens > MAX_MODEL_LEN else f"{used_percent:.1f}%"
            print(f"initial--token数量: {text_tokens} | MAX_MODEL_LEN: {MAX_MODEL_LEN} ({status})")

            inputs.append({
                "prompt": formatted_prompt,
                "multi_modal_data": {"image": image}
            })
        
        print("[DOMAIN STATS]")
        for k, v in sorted(domain_counter.items()):
            print(f"Domain {k}: {v} 次")
    
        return inputs

    def clean_content_v3(self, text):
        """Enhanced cleaning function to thoroughly remove useless paragraphs and associated whitespace"""
        if not isinstance(text, str):
            return str(text)
        
        text = re.sub(r'\n{3,}', '\n\n', text)
        return '\n'.join([line.strip() for line in text.split('\n') if line.strip()])
    
    def prepare_final_inputs(
        self, 
        queries: List[str],
        images: List[Image.Image],
        search_results: List[List[Dict]],
        message_histories: List[List[Dict[str, Any]]]
    ) ->List[dict]:
        """准备最终生成输入（包含完整上下文）"""
        inputs = []
        for q, img, sr, hist in zip(queries, images, search_results, message_histories):
            messages = []
            if hist:
                messages.extend(hist)
            
            messages.extend([
                {
                    "role": "user",
                    "content": [
                        {"type": "image"},
                        {"type": "text", "text": q}
                    ]
                }
            ])
            
            if context := self.prepare_rag_context(sr):
                messages.append({
                    "role": "user",
                    "content": f"Relevant search results:\n{context}"
                })
                
            messages.append({
                "role": "user",
                "content": (
                    "You are an image analysis assistant that responds strictly based on visible content and search results. "
                    "Follow these response rules:\n\n"
                    "1. DIRECT ANSWERS ONLY WHEN:\n"
                    "   - Answer is literally visible (text recognition, object count, color identification)\n"
                    "   - Search results have direct answer\n"
                    "2. ALWAYS RESPOND 'I don't know' WHEN ASKED ABOUT:\n"
                    "   - Prices/offers\n"
                    "   - Medical/legal advice\n"
                    "   - Brand policies\n"
                    "   - Comparisons\n"
                    "   - Future predictions\n\n"
                    "Keep responses under 30 words. Never suggest alternatives."
                )
            })
            
            formatted_prompt = self.tokenizer.apply_chat_template(
                messages,
                add_generation_prompt=True,
                tokenize=False
            )
            text_tokens = len(self.tokenizer.encode(formatted_prompt, add_special_tokens=False))
            used_percent = text_tokens / MAX_MODEL_LEN * 100
            status = "⚠️ OVERLIMIT" if text_tokens > MAX_MODEL_LEN else f"{used_percent:.1f}%"
            print(f"final--token数量: {text_tokens} | MAX_MODEL_LEN: {MAX_MODEL_LEN} ({status})")
            
            inputs.append({
                "prompt": formatted_prompt,
                "multi_modal_data": {"image": img}
            })
        return inputs

    def remove_nulls_and_placeholders(self, data):
        """递归清理字典中的无效值"""
        if isinstance(data, dict):
            cleaned = {}
            for k, v in data.items():
                if v in (None, "<>", "null", [], {}) or (
                    isinstance(v, str) and v.strip() in ("", "<>")
                ):
                    continue
                cleaned_v = self.remove_nulls_and_placeholders(v)
                if isinstance(cleaned_v, (dict, list)) and not cleaned_v:
                    continue
                cleaned[k] = cleaned_v
            return cleaned
        elif isinstance(data, list):
            cleaned_list = []
            for item in data:
                cleaned_item = self.remove_nulls_and_placeholders(item)
                if cleaned_item not in (None, [], {}):
                    cleaned_list.append(cleaned_item)
            return cleaned_list
        else:
            return data

    def batch_generate_response(
        self,
        queries: List[str],
        images: List[Image.Image],
        message_histories: List[List[Dict[str, Any]]],
    ) -> List[str]:
        """两阶段生成流程（只使用图像搜索）"""
        # 第一阶段：生成搜索查询
        initial_inputs = self.prepare_initial_inputs(queries, images, message_histories)
        initial_outputs = self.llm.generate(
            initial_inputs,
            sampling_params=vllm.SamplingParams(
                temperature=0.1,
                top_p=0.9,
                max_tokens=75,
                skip_special_tokens=True
            )
        )
        search_queries = [out.outputs[0].text.strip() for out in initial_outputs]
        
        # 获取图像搜索结果
        image_search_results = [
            self.get_image_search_results(img, k=2)
            for img in images
        ]
        
        print(f"[DEBUG] 准备生成最终输入，问题数量: {len(queries)}")
        print(f"[DEBUG] 图像搜索结果数量: {len(image_search_results)}")
        
        # 第二阶段：生成最终回答
        final_inputs = self.prepare_final_inputs(
            queries, images, image_search_results, message_histories
        )
        print(f"[DEBUG] 最终输入数量: {len(final_inputs)}")  

        final_outputs = self.llm.generate(
            final_inputs,
            sampling_params=vllm.SamplingParams(
                temperature=0.1,
                top_p=0.9,
                max_tokens=MAX_GENERATION_TOKENS,
                skip_special_tokens=True
            )
        )
        
        return [out.outputs[0].text.strip() for out in final_outputs]