class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return True

            for end in range(start + 1, len(s)+ 1):
                if s[start:end] in wordSet and dfs(end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        return dfs(0)