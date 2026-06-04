class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_res = max(max_res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_res
