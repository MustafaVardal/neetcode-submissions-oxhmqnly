class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        maxVal = float('-inf')
        listA = []

        res = []

        while r < k:
            listA.append(nums[r])
            r += 1
        res.append(max(listA))

        while r < len(nums):
            listA.pop(0)
            listA.append(nums[r])
            res.append(max(listA))
            r+=1
            l+=1

        return res