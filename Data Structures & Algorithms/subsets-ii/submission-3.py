class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subSet, curSet = [], []
        

        def dfs( i, nums, curSet, subSet):
            if i >= len(nums):
                subSet.append(list(curSet))
                return
            curSet.append(nums[i])
            dfs(i+ 1, nums, curSet, subSet)
            curSet.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, nums, curSet, subSet)
        dfs(0, nums, curSet, subSet)
        return subSet