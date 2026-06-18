"""
Кластеризация: KMeans, DBSCAN, метод локтя
"""
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler

def kmeans_cluster(X, n_clusters):
    """KMeans кластеризация."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    km = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)
    return labels, km

def dbscan_cluster(X, eps=0.5, min_samples=5):
    """DBSCAN кластеризация."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    db = DBSCAN(eps=eps, min_samples=min_samples)
    labels = db.fit_predict(X_scaled)
    return labels

def elbow_method(X, max_k=10):
    """Метод локтя для выбора числа кластеров."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    inertias = []
    for k in range(1, max_k + 1):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X_scaled)
        inertias.append(km.inertia_)
    plt.plot(range(1, max_k + 1), inertias, 'bo-')
    plt.xlabel('k')
    plt.ylabel('Инерция')
    plt.title('Метод локтя')
    plt.show()
