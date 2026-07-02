class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = defaultdict(int)

        for s in s1:    
            s1_count[s] += 1
        
        window_freq = defaultdict(int)
        for i in range(len(s1)):
            window_freq[s2[i]] += 1
        
        if s1_count == window_freq:
            return True

        l = 0
        r = len(s1) - 1

        while r < len(s2) - 1:
            r += 1

            window_freq[s2[r]] += 1
            
            window_freq[s2[l]] -= 1

            if window_freq[s2[l]] == 0:
                del window_freq[s2[l]]
            
            l += 1

            if s1_count == window_freq:
                return True

        return False
