"""
Утилиты для преобразования структур данных
"""
class DictRowMapper:
    """Превращает список полей и строк в итератор словарей."""
    def __init__(self, fields=None, rows=None):
        self.fields = fields or []
        self.rows = rows or []
    
    def __iter__(self):
        for row in self.rows:
            if not row or len(row) < len(self.fields):
                continue
            yield {self.fields[i]: row[i] for i in range(len(self.fields))}
    
    def from_table(self, table):
        """Загружает данные из списка списков (первая строка — заголовки)."""
        if table:
            self.fields = table[0]
            self.rows = table[1:]
        return self

def flatten_nested(data, parent_key="", sep="."):
    """
    Рекурсивно разворачивает вложенные словари и списки в плоский словарь.
    Пример: {'a': {'b': 1}} -> {'a.b': 1}
    """
    result = {}
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            result.update(flatten_nested(value, new_key, sep))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, (dict, list)):
                    result.update(flatten_nested({str(i): item}, new_key, sep))
                else:
                    result[f"{new_key}.{i}"] = item
        else:
            result[new_key] = value
    return result
