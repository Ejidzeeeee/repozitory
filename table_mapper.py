"""
Класс-итератор TableMapper: превращает списки в словари
"""
class TableMapper:
    def __init__(self, data):
        if not data:
            self.fields = []
            self.rows = []
        else:
            self.fields = data[0]
            self.rows = data[1:]
    
    def __iter__(self):
        for row in self.rows:
            if not row:
                continue
            if len(row) < len(self.fields):
                continue
            yield {self.fields[i]: row[i] for i in range(len(self.fields))}
