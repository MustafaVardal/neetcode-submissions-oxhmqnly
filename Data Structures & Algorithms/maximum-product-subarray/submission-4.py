class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = smallest = res = nums[0]

        for num in nums[1:]:
            if num < 0:
                largest, smallest = smallest, largest

            largest = max(num, num * largest)
            smallest = min(num, num * smallest)

            res = max(res, largest)

        return res