class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uni= set()

        for i in range(len(nums)):
            if  nums[i] in uni:
                return True
            else:
                uni.add(nums[i])
        return False
