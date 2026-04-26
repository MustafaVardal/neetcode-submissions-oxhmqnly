class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, houses):
        memo = {}

        def dfs(i):
            if i >= len(houses):
                return 0
            if i in memo:
                return memo[i]

            rob = houses[i] + dfs(i + 2)

            skip = dfs(i + 1)

            memo[i] = max(rob, skip)
            return memo[i]
        return dfs(0)

