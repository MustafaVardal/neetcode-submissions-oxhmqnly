class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for i in range(n + 1)]

        counter = Counter(nums)

        for num, c in counter.items():
            bucket[c].append(num)

        res = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

        print(bucket)