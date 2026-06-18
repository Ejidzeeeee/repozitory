"""
Тематическое моделирование LDA, визуализация через pyLDAvis
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pyLDAvis
import pyLDAvis.sklearn
import pandas as pd

def train_lda(texts, n_topics=3, max_features=1000):
    """Обучает LDA на корпусе текстов."""
    vectorizer = CountVectorizer(max_features=max_features, stop_words='english')
    X = vectorizer.fit_transform(texts)
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(X)
    return lda, vectorizer, X

def get_top_words(lda, vectorizer, n_words=5):
    """Возвращает топ-слов для каждой темы."""
    feature_names = vectorizer.get_feature_names_out()
    topics = {}
    for topic_idx, topic in enumerate(lda.components_):
        top_indices = topic.argsort()[-n_words:][::-1]
        top_words = [feature_names[i] for i in top_indices]
        topics[f"Тема {topic_idx+1}"] = top_words
    return topics

def get_dominant_topic(lda, X):
    """Определяет доминирующую тему для каждого документа."""
    topic_dist = lda.transform(X)
    return topic_dist.argmax(axis=1)

def visualize_lda(lda, X, vectorizer):
    """Визуализирует LDA через pyLDAvis."""
    return pyLDAvis.sklearn.prepare(lda, X, vectorizer)
