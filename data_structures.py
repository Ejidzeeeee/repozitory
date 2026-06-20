"""
Универсальные структуры данных и алгоритмы
"""
from collections import OrderedDict

class UniqueList:
    """Сохраняет элементы в порядке первого появления, удаляя дубликаты."""
    def __init__(self, data=None):
        self._items = []
        self._seen = set()
        if data:
            for x in data:
                self.append(x)
    
    def append(self, x):
        if x not in self._seen:
            self._seen.add(x)
            self._items.append(x)
    
    def __iter__(self):
        return iter(self._items)
    
    def __len__(self):
        return len(self._items)
    
    @property
    def items(self):
        return self._items.copy()

class LRUCache:
    """Кэш с вытеснением самых старых элементов."""
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.cap = capacity
    
    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

def sort_inplace(arr):
    """Быстрая сортировка (in-place) с random pivot."""
    import random
    if len(arr) <= 1:
        return arr
    stack = [(0, len(arr)-1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            p = random.randint(low, high)
            arr[low], arr[p] = arr[p], arr[low]
            pivot = arr[low]
            left, right = low+1, high
            while left <= right:
                while left <= right and arr[left] <= pivot:
                    left += 1
                while left <= right and arr[right] > pivot:
                    right -= 1
                if left < right:
                    arr[left], arr[right] = arr[right], arr[left]
            arr[low], arr[right] = arr[right], arr[low]
            stack.append((low, right-1))
            stack.append((right+1, high))
    return arr
