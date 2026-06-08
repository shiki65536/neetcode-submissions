class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(start, end):
            if start == end == n:
                res.append("".join(stack))
            if start < n:
                stack.append("(")
                backtrack(start + 1, end)
                stack.pop()
            if end < start:
                stack.append(")")
                backtrack(start, end+1)
                stack.pop()
        
        backtrack(0, 0)
        return res







        # def backtrack(openN, closeN):
        #     if openN == closeN == n:
        #         res.append("".join(stack))
        #     if openN < n:
        #         stack.append("(")
        #         backtrack(openN + 1, closeN)
        #         stack.pop()
        #     if closeN < openN:
        #         stack.append(")")
        #         backtrack(openN, closeN + 1)
        #         stack.pop()

        # backtrack(0, 0)
        # return res