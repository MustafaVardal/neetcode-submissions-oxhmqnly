class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        LAST_ROW, LAST_COL = ROWS- 1, COLS - 1
        if obstacleGrid[0][0] == 1 or obstacleGrid[LAST_ROW][LAST_COL] == 1:
            return 0
        
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        dp[LAST_ROW][LAST_COL] = 1

        for r in range(LAST_ROW, -1, -1):
            for c in range(LAST_COL, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r+ 1][c]
                    dp[r][c] += dp[r][c+1]
        return dp[0][0]