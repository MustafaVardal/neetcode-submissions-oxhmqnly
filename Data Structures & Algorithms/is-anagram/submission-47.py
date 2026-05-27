class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sD= defaultdict(int)
        tD= defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sD[s[i]] += 1
            tD[t[i]] += 1

        return sD == tD