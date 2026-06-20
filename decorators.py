"""
Декораторы для логирования и замеров времени
"""
import time
from functools import wraps

def log_call(func):
    """Декоратор: печатает имя функции, аргументы и результат."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[CALL] {func.__name__}")
        if args:
            print(f"  args: {args}")
        if kwargs:
            print(f"  kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"  result: {result}")
        return result
    return wrapper

def timer(func):
    """Декоратор: замеряет время выполнения в мс."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"[TIME] {func.__name__}: {elapsed:.2f} мс")
        return result
    return wrapper

def count_unique(items):
    """Возвращает элементы, встречающиеся ровно один раз (сохраняя порядок)."""
    from collections import Counter
    counts = Counter(items)
    return [x for x in items if counts[x] == 1]
