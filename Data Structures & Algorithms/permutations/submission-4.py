class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            nextperm = []
            for p in perms:
                for i in range(len(p)+ 1):
                    pcopy = p[:]
                    pcopy.insert(i, num)
                    nextperm.append(pcopy)
            perms = nextperm
        return perms