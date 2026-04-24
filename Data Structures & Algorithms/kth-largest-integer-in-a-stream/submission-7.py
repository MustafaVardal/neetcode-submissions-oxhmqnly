class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        print(self.minHeap)


        # 1, 2, 3, 3 | k = 3
        # 0  1  2  3
        # k  k-1 k-2 

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap)> self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
