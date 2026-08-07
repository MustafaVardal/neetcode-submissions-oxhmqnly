class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxFreq = [-c for c in count.values()]

        heapq.heapify(maxFreq)
        q  = deque()

        times =0
        while maxFreq or q:
            times += 1
            if maxFreq:
                cnt = 1 + heapq.heappop(maxFreq)

                if cnt:
                    q.append([cnt, times + n])
            if q and q[0][1] == times:
                heapq.heappush(maxFreq, q.popleft()[0])
        return times