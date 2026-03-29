class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        res= []
        rows, cols = len(heights), len(heights[0])

        for j in range(cols):
            self.helper(0, j, rows, cols, heights, pac)
        for i in range(rows):
            self.helper(i, 0, rows, cols, heights, pac)
        for y in range(cols):
            self.helper(rows - 1, y, rows, cols, heights, atl)
        for x in range(rows):
            self.helper(x, cols - 1, rows, cols, heights, atl)
        for x, y in pac:
            if (x, y) in atl:
                res.append([x, y])
        return res



    def helper(self, i, j, row, col,heights, visited):
        if (i, j) in visited:
            return 
        visited.add((i, j))
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            ni, nj = i + dx, j + dy

            if (0 <= ni < row) and (0 <= nj < col) and heights[i][j] <= heights[ni][nj]:
                self.helper(ni, nj, row, col, heights, visited)

        