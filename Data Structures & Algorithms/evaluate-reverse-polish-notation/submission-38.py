class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        operators = ['+','-','*','/']
        for token in tokens:

            if token in operators:
                if token == operators[0]:
                    a, b = res.pop(), res.pop()
                    res.append(a + b) 
                elif token == operators[1]:
                    a, b = res.pop(), res.pop()
                    res.append(b - a)
                elif token == operators[2]:
                    a, b = res.pop(), res.pop()
                    res.append(a * b)
                elif token == operators[3]:
                    a, b = res.pop(), res.pop()
                    res.append(int(float(b) / a))
            
            else:
                res.append(int(token))

        return res[0]