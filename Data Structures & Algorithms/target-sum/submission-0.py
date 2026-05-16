class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ### [1 , 2]
        cache = {}


        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            
            if (i, total) in cache:
                return cache[(i, total)]

            add = dfs(i + 1, total + nums[i])
            sub = dfs(i + 1, total - nums[i])

            cache[(i, total)] = add + sub
            return cache[(i, total)]

        return dfs(0, 0)

        ## cache = {}

        ## def dfs (i: int, total: int, sum: bool):
                ## if i >= len(nums):
                    ## return 0
                ## if (i, sum) in cache:
                    ## return cache[(i, sum)]
                
                ## cache[(i, sum)] = 
