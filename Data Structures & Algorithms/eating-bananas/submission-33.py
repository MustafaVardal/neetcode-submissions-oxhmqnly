
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r 
        while l <= r:
            total_time = 0
            speed = l + (r - l) // 2

            for p in piles:
                total_time += math.ceil(float(p) / speed)

            if total_time <= h:
                res = speed
                r = speed - 1
            else:
                l = speed + 1
        return res