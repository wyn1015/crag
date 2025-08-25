import json
import os
from typing import List, Dict, Any
from domain_class import DomainClassifier  # 确保domain_classifier.py在同一目录

def load_json_with_retry(file_path: str, max_retries=3) -> List[Dict[str, Any]]:
    """安全加载JSON文件，支持重试机制[4,6](@ref)"""
    for _ in range(max_retries):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"加载失败: {str(e)}，剩余重试次数{max_retries - _ -1}")
    raise RuntimeError(f"无法加载文件: {file_path}")

def predict_domains(queries: List[str], model_path: str) -> List[int]:
    """批量执行领域分类预测[7](@ref)"""
    classifier = DomainClassifier(model_path)
    return [classifier.predict(q) for q in queries]

def save_results_with_backup(data: List[Dict], output_path: str):
    """安全保存结果文件，包含临时文件写入和原子替换[4,6](@ref)"""
    temp_path = output_path + ".tmp"
    try:
        with open(temp_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(temp_path, output_path)  # 原子操作避免写入中断
    except IOError as e:
        print(f"保存失败: {str(e)}")
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    # 配置参数（根据实际路径修改）
    INPUT_JSON = "/home/wangyanan/transformer-code1/output/output_image5.json"
    MODEL_PATH = "/home/wangyanan/transformer-code1/clip_roberta/roberta/saved_model"  # 替换实际模型路径
    OUTPUT_JSON = "/home/wangyanan/transformer-code1/meta-crag-submission copy/agents/domain/predictions.json"

    try:
        # 1. 加载数据[1,4](@ref)
        raw_data = load_json_with_retry(INPUT_JSON)
        
        # 2. 提取query字段[7](@ref)
        queries = [item["query"] for item in raw_data if "query" in item]
        
        # 3. 执行预测[7](@ref)
        predictions = predict_domains(queries, MODEL_PATH)
        
        # 4. 合并结果[5](@ref)
        for data_item, pred in zip(raw_data, predictions):
            data_item["predicted_domain"]= pred
        
        # 5. 保存结果[3,6](@ref)
        save_results_with_backup(raw_data, OUTPUT_JSON)
        print(f"成功处理{len(raw_data)}条数据，结果已保存至{OUTPUT_JSON}")

    except Exception as e:
        print(f"处理过程中发生错误: {str(e)}")
        if 'raw_data' in locals():
            print("尝试保存已处理的部分结果...")
            save_results_with_backup(raw_data, "partial_"+OUTPUT_JSON)