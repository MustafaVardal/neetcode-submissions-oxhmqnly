class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []

        for i, height in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > height:
                idx, sHeight = stack.pop()
                largest = max(largest, sHeight * (i - idx))
                start = idx
            stack.append([start, height])

        for i, h in stack:
            width = len(heights) - i
            largest = max(largest, h * width)
        return largest
