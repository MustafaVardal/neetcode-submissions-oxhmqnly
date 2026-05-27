class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_by = defaultdict(list)

        for word in strs:
            letter_filtering = [0] * 26
            for ch in word:
                #print((letter_filtering))
                letter_filtering[ord(ch) - ord('a')] += 1
            group_by[tuple(letter_filtering)].append(word)
        return list(group_by.values())