class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = "".join(char for char in s if char.isalnum()).lower()
        l = 0
        r = len(clean_string) - 1

        while l < r:
            if clean_string[l] != clean_string[r]:
                return False
            l += 1
            r -= 1
        return True