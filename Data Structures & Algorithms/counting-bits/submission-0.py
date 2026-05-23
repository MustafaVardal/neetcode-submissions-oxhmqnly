class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        res.append(0)
        i = 1
        while i <= n:
            count = 0
            temp = i
            while temp > 0:
                if temp & 1 == 1:
                    count += 1
                temp >>= 1
            
            res.append(count)
            i += 1
        return res