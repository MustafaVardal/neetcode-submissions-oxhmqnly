class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = (rows * cols) - 1
        
        while left <= right:
            m = left + (right - left) // 2

            row = m // cols
            col = m % cols

            if target > matrix[row][col]:
                left = m + 1
            elif target < matrix[row][col]:
                right = m - 1
            else:
                return True
        return False