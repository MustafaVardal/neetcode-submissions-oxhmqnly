class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            left, right= 0, len(tails) - 1
            while left <= right:
                m = left + (right - left) // 2
                if tails[m] < num:
                    left =  m + 1
                else:
                    right = m - 1

            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num
        return len(tails) 