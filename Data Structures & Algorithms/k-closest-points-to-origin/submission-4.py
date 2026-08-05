from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            
            x = point[0]
            y = point[1]
            
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist,x, y])

            if len(maxHeap)> k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res
            
            