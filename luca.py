"""
Числа Люка: генератор, рекурсия, мемоизация, замер времени
"""
import time
from functools import lru_cache

def generate_sequence(n):
    """Генератор первых n чисел Люка."""
    a, b = 2, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def lucas_recursive(k):
    """Рекурсивное вычисление k-го числа Люка (без оптимизации)."""
    if k == 0:
        return 2
    if k == 1:
        return 1
    return lucas_recursive(k - 1) + lucas_recursive(k - 2)

@lru_cache(maxsize=None)
def lucas_memoized(k):
    """Рекурсивное вычисление с мемоизацией."""
    if k == 0:
        return 2
    if k == 1:
        return 1
    return lucas_memoized(k - 1) + lucas_memoized(k - 2)

def compare_lucas_performance(n):
    """Сравнивает три способа получения первых n чисел."""
    # Генератор
    start = time.time()
    list(generate_sequence(n))
    gen_time = time.time() - start
    
    # Рекурсия без оптимизации (только для маленьких n!)
    if n <= 35:
        start = time.time()
        [lucas_recursive(i) for i in range(n)]
        rec_time = time.time() - start
    else:
        rec_time = float('inf')
        print("Рекурсия без мемоизации пропущена (слишком долго)")
    
    # Рекурсия с мемоизацией
    start = time.time()
    [lucas_memoized(i) for i in range(n)]
    memo_time = time.time() - start
