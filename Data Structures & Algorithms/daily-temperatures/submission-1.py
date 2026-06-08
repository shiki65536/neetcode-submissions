class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            if temperatures[i-1] < temperatures[i]:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    pre = stack.pop()
                    day = i - pre
                    res[pre] = day
            stack.append(i)

        return res
