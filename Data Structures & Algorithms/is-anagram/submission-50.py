class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_T = defaultdict(int)
        letter_S = defaultdict(int)

        # edge case 
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            letter_T[ord(t[i]) - ord('a')] += 1
            letter_S[ord(s[i]) - ord('a')] += 1 

        return letter_S == letter_T             