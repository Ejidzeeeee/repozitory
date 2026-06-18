"""
Обнаружение аномалий: Isolation Forest, IQR, Z-score
"""
import numpy as np
from sklearn.ensemble import IsolationForest
from scipy import stats

def find_anomalies_isolation(X, contamination=0.05):
    """Isolation Forest для поиска аномалий."""
    model = IsolationForest(contamination=contamination, random_state=42)
    pred = model.fit_predict(X)  # 1 = норма, -1 = аномалия
    anomalies = np.where(pred == -1)[0]
    print(f"Найдено {len(anomalies)} аномалий")
    return anomalies, model

def find_anomalies_zscore(df, col, threshold=3):
    """Аномалии по Z-оценке (|z| > threshold)."""
    z = np.abs(stats.zscore(df[col].dropna()))
    anomalies = df[df[col].notna() & (z > threshold)]
    print(f"Найдено {len(anomalies)} аномалий в {col}")
    return anomalies

def find_anomalies_iqr(df, col, multiplier=1.5):
    """Аномалии по IQR."""
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    low = Q1 - multiplier * IQR
    high = Q3 + multiplier * IQR
    anomalies = df[(df[col] < low) | (df[col] > high)]
    print(f"Найдено {len(anomalies)} аномалий в {col}")
    return anomalies
