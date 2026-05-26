class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # jar jam
        # valid anagram?
        dictT = defaultdict(int)
        dictS = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):

            dictS[ord(s[i])] += 1
            dictT[ord(t[i])] += 1

        return dictS == dictT
     
    
        


        # jar --- > all word need to use ( raj, arj, ajr)
        # it should be same lenght otherwise the output of the value definetly different.
        # For this we can add one edge case too.
            # for each word we need to get and we need to gave them some number w
    
              # if yes then return True. #0000 So t can be unsorted order. 


            # else:
            # return False