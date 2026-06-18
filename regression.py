"""
Сравнение моделей регрессии: линейная, случайный лес
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def compare_regressors(X_train, X_test, y_train, y_test):
    """Сравнивает линейную регрессию и случайный лес."""
    models = {
        'Линейная': LinearRegression(),
        'Случайный лес': RandomForestRegressor(random_state=42)
    }
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        print(f"{name}: MAE={mae:.3f}, RMSE={rmse:.3f}, R2={r2:.3f}")

def plot_predictions(y_test, y_pred, title="Реальные vs Предсказанные"):
    """График реальных vs предсказанных значений."""
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())
    plt.plot([min_val, max_val], [min_val, max_val], 'r--')
    plt.xlabel('Реальные')
    plt.ylabel('Предсказанные')
    plt.title(title)
    plt.show()
