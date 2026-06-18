"""
Word2Vec и граф знаний через networkx
"""
import networkx as nx
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

def train_word2vec(sentences, vector_size=50, window=5, min_count=1):
    """Обучение Word2Vec на корпусе предложений."""
    model = Word2Vec(sentences, vector_size=vector_size, window=window, min_count=min_count)
    return model

def build_graph(model, threshold=0.85):
    """Строит граф, где рёбра = косинусная близость > threshold."""
    words = list(model.wv.index_to_key)
    if len(words) < 2:
        print("Слишком мало слов для графа")
        return nx.Graph()
    vectors = [model.wv[w] for w in words]
    sim = cosine_similarity(vectors)
    G = nx.Graph()
    G.add_nodes_from(words)
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if sim[i][j] > threshold:
                G.add_edge(words[i], words[j])
    return G

def plot_graph(G, title="Граф знаний"):
    """Визуализация графа."""
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=8)
    plt.title(title)
    plt.show()

def most_similar_words(model, word, top_n=5):
    """Топ-N ближайших слов."""
    try:
        return model.wv.most_similar(word, topn=top_n)
    except KeyError:
        print(f"Слово '{word}' не найдено в модели")
        return []
