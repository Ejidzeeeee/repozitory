"""
EDA: быстрый анализ данных, пропуски, выбросы, графики
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def quick_eda(df):
    """Печатает размер, типы, пропуски, статистику. Строит графики."""
    print("Размер:", df.shape)
    print("\nТипы данных:\n", df.dtypes.value_counts())
    
    missing = df.isnull().sum()
    missing_pct = missing / len(df) * 100
    miss = pd.DataFrame({'пропуски': missing, '%': missing_pct})
    print("\nПропуски:\n", miss[miss['пропуски'] > 0])
    
    num_cols = df.select_dtypes(include=[np.number]).columns
    if len(num_cols) > 0:
        print("\nСтатистика:\n", df[num_cols].describe())
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        df[num_cols].hist(bins=20, ax=axes[0, 0])
        axes[0, 0].set_title('Гистограммы')
        sns.heatmap(df[num_cols].corr(), annot=True, ax=axes[0, 1])
        axes[0, 1].set_title('Корреляции')
        df[num_cols].boxplot(ax=axes[1, 0])
        axes[1, 0].set_title('Ящики с усами')
        axes[1, 1].axis('off')
        plt.tight_layout()
        plt.show()

def detect_outliers_iqr(df, col, multiplier=1.5):
    """Выбросы по межквартильному размаху (IQR)."""
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    low = Q1 - multiplier * IQR
    high = Q3 + multiplier * IQR
    return df[(df[col] < low) | (df[col] > high)]

def fill_missing(df, method='median'):
    """Заполняет пропуски в числовых столбцах median или mean."""
    df2 = df.copy()
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        if df[col].isnull().any():
            if method == 'median':
                df2[col].fillna(df[col].median(), inplace=True)
            else:
                df2[col].fillna(df[col].mean(), inplace=True)
    return df2
