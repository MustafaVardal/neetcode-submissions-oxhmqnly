class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        reverseOrder = {
            ']':'[',
            '}':'{',
            ')':'(',
        }

        for c in s:
            if c in reverseOrder:
                if stack and stack[-1] == reverseOrder[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if len(stack)== 0 else False