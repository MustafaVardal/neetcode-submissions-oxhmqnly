class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.maxHeap = []
        for num in nums:
            self.add(num)


    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, val)
        if len(self.maxHeap) > self.k:
            heapq.heappop(self.maxHeap)
            
        return self.maxHeap[0]
