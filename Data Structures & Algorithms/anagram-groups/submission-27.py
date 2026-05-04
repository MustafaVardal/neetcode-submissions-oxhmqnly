class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word = defaultdict(list)

        for s in strs:
            letter = [0] * 26
            for ch in s:
                letter[ord(ch) - ord('a')] += 1
            
            word[tuple(letter)].append(s)
        
        return list(word.values())