"""
Математические утилиты: последовательности, площади фигур
"""
import math
import time
from functools import lru_cache

def generate_recurrence(n, a0, a1):
    """
    Генератор для рекуррентных последовательностей вида: 
    a(n) = a(n-1) + a(n-2)
    """
    a, b = a0, a1
    for _ in range(n):
        yield a
        a, b = b, a + b

def recurrence_memoized(k, a0, a1):
    """Рекурсивное вычисление с мемоизацией для рекуррентных последовательностей."""
    @lru_cache(maxsize=None)
    def _rec(n):
        if n == 0:
            return a0
        if n == 1:
            return a1
        return _rec(n-1) + _rec(n-2)
    return _rec(k)

def measure_time(func, *args, **kwargs):
    """Замеряет время выполнения функции."""
    start = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - start
    return result, elapsed

class Shape:
    def area(self):
        return 0

def square_area(side):
    return side ** 2

def circle_area(radius):
    return math.pi * radius ** 2

def triangle_area(a, b):
    return (a * b) / 2
