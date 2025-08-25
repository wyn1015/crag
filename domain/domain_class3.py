# domain_classifier.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os
DOMAIN_MAP = {
    0: "animal",
    1: "shopping",
    2: "plants and gardening",
    3: "general object recognition",
    5: "math and science",
    6: "vehicle",
    7: "text understanding",
    8: "brand",
    9: "food",
    10: "others",
    11: "book"
}


class DomainClassifier:
    def __init__(self, model_path):
        """加载预训练domain分类模型"""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.model.to(self.device)
        self.model.eval()
        
    def predict(self, text):
        """预测文本的domain类别"""
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
            predicted_class = torch.argmax(probs, dim=1).item()
            
        return predicted_class