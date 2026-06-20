"""
Утилиты для работы с матрицами
"""
class MatrixHelper:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0
    
    def row(self, i):
        if 0 <= i < self.rows:
            return self.matrix[i]
        print(f"Индекс строки {i} вне диапазона (0-{self.rows-1})")
        return None
    
    def col(self, j):
        if 0 <= j < self.cols:
            return [self.matrix[i][j] for i in range(self.rows)]
        print(f"Индекс столбца {j} вне диапазона (0-{self.cols-1})")
        return None
    
    def max_value(self):
        if not self.matrix:
            return None
        return max(max(row) for row in self.matrix)
    
    def min_value(self):
        if not self.matrix:
            return None
        return min(min(row) for row in self.matrix)
    
    def transpose(self):
        if not self.matrix:
            return []
        return [[self.matrix[i][j] for i in range(self.rows)] for j in range(self.cols)]
