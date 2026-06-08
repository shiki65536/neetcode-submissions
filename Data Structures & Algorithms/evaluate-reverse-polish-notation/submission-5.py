class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda x, y : x + y,
            "-": lambda x, y : x - y,
            "*": lambda x, y : x * y,
            "/": lambda x, y : int(x /y),
        }
        
        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                right = stack.pop()
                left = stack.pop()
                ope = operators[t]
                res = ope(left, right)
                stack.append(res)
        return stack[-1]