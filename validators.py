"""
Утилиты для валидации данных и работы с файлами
"""
def validate_input(data, schema):
    """
    Проверяет, что данные соответствуют схеме.
    schema: {'field': {'type': int, 'required': True, 'allowed': [1,2,3]}}
    """
    errors = []
    for field, rules in schema.items():
        if rules.get('required', False) and field not in data:
            errors.append(f"Поле '{field}' обязательно")
            continue
        if field in data:
            value = data[field]
            if 'type' in rules and not isinstance(value, rules['type']):
                errors.append(f"Поле '{field}' должно быть типа {rules['type'].__name__}")
            if 'allowed' in rules and value not in rules['allowed']:
                errors.append(f"Поле '{field}' должно быть одним из {rules['allowed']}")
    return errors

class SafeFileWriter:
    """Контекстный менеджер для записи в файл с обработкой ошибок."""
    def __init__(self, path):
        self.path = path
        self.file = None
        self.bytes_written = 0
    
    def __enter__(self):
        self.file = open(self.path, 'w', encoding='utf-8')
        return self
    
    def write(self, text):
        self.file.write(text)
        self.bytes_written += len(text.encode('utf-8'))
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.file.write(f"\n[Ошибка] {exc_val}\n")
        self.file.close()
        print(f"Записано байт: {self.bytes_written}")
        return False
