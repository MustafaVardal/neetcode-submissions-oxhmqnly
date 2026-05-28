class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for i in range(len(nums)):
            counter[nums[i]] += 1

        for key, val in counter.items():
            buckets[val].append(key)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
