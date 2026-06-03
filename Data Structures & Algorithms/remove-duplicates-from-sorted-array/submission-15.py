class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        l = 0
        r = 0
        
        while r < len(nums):
            if r == 0 or nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l