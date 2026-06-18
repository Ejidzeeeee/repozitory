"""
Масштабирование, кодирование, разделение выборки
"""
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split

def scale_data(X_train, X_test, method='standard'):
    """Масштабирование: standard или minmax."""
    if method == 'standard':
        scaler = StandardScaler()
    else:
        scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler

def encode_cat(df, cols):
    """Label encoding для указанных столбцов."""
    df2 = df.copy()
    le_dict = {}
    for col in cols:
        le = LabelEncoder()
        df2[col] = le.fit_transform(df2[col].astype(str))
        le_dict[col] = le
    return df2, le_dict

def split_train_test(X, y, test_size=0.2, random_state=42):
    """Разделение на train/test."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
