"""
Сравнение моделей классификации: дерево, лес, логистическая регрессия
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

def compare_models(X_train, X_test, y_train, y_test):
    """Сравнивает три модели и выводит Accuracy и F1."""
    models = {
        'Дерево': DecisionTreeClassifier(random_state=42),
        'Лес': RandomForestClassifier(random_state=42),
        'Логистическая': LogisticRegression(max_iter=1000, random_state=42)
    }
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')
        results[name] = {'Accuracy': acc, 'F1': f1}
        print(f"{name}: Accuracy={acc:.3f}, F1={f1:.3f}")
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred), "\n")
    return results

def get_feature_importance(model, feature_names):
    """Важность признаков для моделей, у которых есть feature_importances_."""
    if hasattr(model, 'feature_importances_'):
        importance = model.feature_importances_
        for name, imp in zip(feature_names, importance):
            print(f"{name}: {imp:.4f}")
        return importance
    else:
        print("У модели нет feature_importances_")
        return None
