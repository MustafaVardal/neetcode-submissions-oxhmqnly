class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, mid, right = [], newInterval, []
        for interval in intervals:
            if interval[1] < mid[0]:
                left.append(interval)
            elif interval[0] > mid[1]:
                right.append(interval)
            else:
                mid[0] = min(mid[0], interval[0])
                mid[1] = max(mid[1], interval[1])
        return left + [mid] + right