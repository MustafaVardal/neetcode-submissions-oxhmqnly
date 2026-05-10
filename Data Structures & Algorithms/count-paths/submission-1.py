class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
 #       def dfs(r, c, rows, cols):
 #           if r == rows or c == cols:
 #               return 0
 #           if r == rows - 1 and  c == cols - 1:
 #               return 1
            
 #           return  dfs(r+1, c, rows, cols) + dfs(r, c+1, rows, cols)

        #return dfs( 0, 0, m, n)


        def memo(r, c, rows, cols, cache):
            if r == rows or c == cols:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            if cache[r][c] > 0:
                return cache[r][c]

            cache[r][c] = (memo(r+1, c, rows, cols, cache) + memo(r, c +1, rows, cols, cache))
            return cache[r][c]
        
        return memo(0, 0, m, n, [[0] * n for i in range(m)])