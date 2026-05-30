class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.store = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                self.store[r + 1][c + 1] = matrix[r][c] + self.store[r][c + 1] + self.store[r + 1][c] - self.store[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:        
        return self.store[row2 + 1][col2 + 1] - self.store[row1][col2 + 1] - self.store[row2 + 1][col1] + self.store[row1][col1]