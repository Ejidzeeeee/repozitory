"""
Apriori, one-hot через mlxtend
"""
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

def one_hot_encode(transactions):
    """Преобразует список транзакций в one-hot матрицу."""
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    return df

def find_frequent_itemsets(df, min_support=0.05):
    frequent = apriori(df, min_support=min_support, use_colnames=True)
    return frequent

def generate_rules(frequent, metric="confidence", min_threshold=0.7):
    """Генерирует ассоциативные правила."""
    rules = association_rules(frequent, metric=metric, min_threshold=min_threshold)
    return rules.sort_values('confidence', ascending=False)
