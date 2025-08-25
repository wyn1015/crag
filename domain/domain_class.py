# domain_classifier.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os

# 定义原始domain值到连续索引的映射
RAW_TO_INDEX = {
    1: 0,   # Book → 0
    2: 1,   # Food → 1
    3: 2,   # General object recognition → 2
    4: 3,   # Shopping → 3
    5: 4,   # Plants and Gardening → 4
    6: 5,   # Local Info → 5
    8: 6,   # Default → 6
    9: 7,   # Vehicles → 7
    10: 8,  # Text understanding → 8
    11: 9,  # Animal → 9
    12: 10  # Art → 10
}

# 定义连续索引到原始domain值的反向映射
INDEX_TO_RAW = {v: k for k, v in RAW_TO_INDEX.items()}

# 定义连续索引到类别名称的映射
DOMAIN_MAP = {
    0: "Book",
    1: "Food",
    2: "General object recognition",
    3: "Shopping",
    4: "Plants and Gardening",
    5: "Local Info",
    6: "Default",
    7: "Vehicles",
    8: "Text understanding",
    9: "Animal",
    10: "Art"
}


class DomainClassifier:
    def __init__(self, model_path):
        """加载预训练domain分类模型"""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.model.to(self.device)
        self.model.eval()
        
    def predict(self, text, return_raw=True, return_name=False):
        """
        预测文本的domain类别
        
        参数:
        text (str): 要分类的文本
        return_raw (bool): 是否返回原始domain值 (默认True)
        return_name (bool): 是否返回类别名称 (默认False)
        
        返回:
        如果 return_raw 和 return_name 都为 False，返回连续索引
        如果 return_raw 为 True，返回原始domain值
        如果 return_name 为 True，返回类别名称
        如果两者都为 True，返回元组 (原始domain值, 类别名称)
        """
        inputs = self.tokenizer(
            text,
            padding=True,
            truncation=True,
            max_length=128,
            return_tensors="pt"
        ).to(self.device)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probs = torch.softmax(logits, dim=1)
            predicted_index = torch.argmax(probs, dim=1).item()
        
        # 根据参数返回不同形式的结果
        if return_raw and return_name:
            raw_domain = INDEX_TO_RAW.get(predicted_index, -1)
            domain_name = DOMAIN_MAP.get(predicted_index, "Unknown")
            return raw_domain, domain_name
        elif return_raw:
            return INDEX_TO_RAW.get(predicted_index, -1)
        elif return_name:
            return DOMAIN_MAP.get(predicted_index, "Unknown")
        else:
            return predicted_index