class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            A = res[-1]
            B = intervals[i]
            
            end_value_first = A[1]
            starting_value_second = B[0]
            if end_value_first >= starting_value_second:
                A[1] = max(end_value_first, B[1])
            else:
                res.append(B)
        return res