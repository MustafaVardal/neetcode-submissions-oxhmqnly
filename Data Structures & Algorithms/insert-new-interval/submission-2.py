class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        
        left, mid, right = [], newInterval,[]

        for i in intervals:
            if i[1] < mid[0]:
                left.append(i)
            elif i[0] > mid[1]:
                right.append(i)
            else:
                mid[0] = min(mid[0], i[0])
                mid[1] = max(mid[1], i[1])
        return left + [mid] + right