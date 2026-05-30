class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest= 0
        seen = set(nums)
        for i in range(len(nums)):
            length = 1
            if nums[i] - 1 not in seen:
                length = 1
            while nums[i] + length in seen:
                length += 1
            longest = max(length, longest)
        return longest