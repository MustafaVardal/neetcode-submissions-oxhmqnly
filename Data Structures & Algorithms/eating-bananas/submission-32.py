import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = r
        while l <= r:
            speed_aprx = l + (r - l) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / speed_aprx)
            if total_time <= h:
                res = speed_aprx
                r = speed_aprx  - 1
            else:
                l = speed_aprx + 1
        return res

        
