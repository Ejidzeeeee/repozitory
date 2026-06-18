"""
Временные ряды: лаги, скользящее среднее, разбивка дат
"""
import pandas as pd

def extract_date_parts(df, date_col):
    """Извлекает год, месяц, день из столбца с датой."""
    df2 = df.copy()
    df2[date_col] = pd.to_datetime(df2[date_col])
    df2['year'] = df2[date_col].dt.year
    df2['month'] = df2[date_col].dt.month
    df2['day'] = df2[date_col].dt.day
    return df2

def create_lag(df, col, n=1):
    """Создаёт лаг-признак (значение из предыдущих строк)."""
    df2 = df.copy()
    df2[f'lag_{n}'] = df2[col].shift(n)
    return df2

def rolling_mean(df, col, window=3):
    """Скользящее среднее."""
    df2 = df.copy()
    df2[f'rolling_{window}'] = df2[col].rolling(window=window).mean()
    return df2
