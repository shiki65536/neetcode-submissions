class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []

        curr = ""
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            elif c == "[":
                count_stack.append(num)
                string_stack.append(curr)
                curr = ""
                num = 0

            elif c == "]":
                repeat = count_stack.pop()
                prev = string_stack.pop()
                curr = prev + curr * repeat

            else:
                curr += c

        return curr
