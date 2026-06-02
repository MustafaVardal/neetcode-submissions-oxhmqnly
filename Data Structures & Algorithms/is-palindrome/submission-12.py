class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join(char for char in s if char.isalnum()).lower()
        l, r =0, len(new_str) -1
        print(new_str)
        while l < r:
            #print(new_str[l], " ", new_str[r])
            if new_str[l] == new_str[r]:
                l += 1
                r -= 1
            else:
                return False
        return True        
                
