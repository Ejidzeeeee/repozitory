"""
Векторизация текста: TF-IDF, CountVectorizer
"""
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def vectorize_tfidf(texts, max_features=None):
    """TF-IDF векторизация."""
    vec = TfidfVectorizer(max_features=max_features)
    X = vec.fit_transform(texts)
    return X, vec

def vectorize_count(texts, max_features=None):
    """CountVectorizer (мешок слов)."""
    vec = CountVectorizer(max_features=max_features)
    X = vec.fit_transform(texts)
    return X, vec
