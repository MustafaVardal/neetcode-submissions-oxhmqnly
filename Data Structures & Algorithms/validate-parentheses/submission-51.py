class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        openToClosed = {
            "]":"[",
            "}":"{",
            ")":"(",
        }

        for p in s:
            if p in openToClosed:
                if not stack or stack.pop() != openToClosed[p]:
                    return False
            else:
                stack.append(p)
        return not stack