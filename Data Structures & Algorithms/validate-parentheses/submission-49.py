class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # comparable data with in lifo
        map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        # filter the data add item key and value reverse side because of lifo
        for p in s:
            
            if p in map:
                # filter data
                if stack and stack[-1] == map[p]:
                    stack.pop()
                    # we match with map ==  stack[-1] 
                    # no need to keep keep continue for new one.                    
                else:
                    return False
                    # not matching then it will be false
                    
            else:
                # add stack.
                stack.append(p)
            
        return True if len(stack) == 0 else False # still in stack then false and also possible not parantesis in stack.
        