class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = []
        for stone in stones:
            heapq.heappush(res, -stone)

        while len(res) > 1:
            
            y = -heapq.heappop(res)
            x = -heapq.heappop(res)

            if x != y:
                heapq.heappush(res, -(y - x))

        return -res[0] if res else 0