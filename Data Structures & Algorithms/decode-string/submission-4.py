class Solution:
    def decodeString(self, s: str) -> str:
        n_stack = []
        w_stack = []
        curr = ""
        num = 0

        for c in s:
            if c.isnumeric():
                num = num*10 + int(c)
            elif c == "[":
                n_stack.append(num)
                w_stack.append(curr)
                curr = ""
                num = 0
            elif c == "]":
                tmp = curr
                curr = w_stack.pop()
                n = n_stack.pop()
                curr = curr + n * tmp
            else:
                curr += c
        
        return curr
