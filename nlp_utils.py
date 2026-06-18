"""
NLP утилиты: токенизация, NER, тональность (через transformers)
"""
import re
from transformers import pipeline

def tokenize(text):
    """Простая токенизация по словам."""
    return re.findall(r'\b\w+\b', text.lower())

def ner_pipeline(text, model_name="cointegrated/rubert-tiny2"):
    """NER через transformers (можно заменить на natasha)."""
    nlp = pipeline("ner", model=model_name, aggregation_strategy="simple")
    return nlp(text)

def sentiment_pipeline(text, model_name="blanchefort/rubert-base-cased-sentiment"):
    """Анализ тональности через transformers."""
    classifier = pipeline("sentiment-analysis", model=model_name)
    return classifier(text)
