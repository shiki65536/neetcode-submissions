class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            offset = columnNumber % 26
            res += chr(ord('A') + offset)
            columnNumber //= 26

        return ''.join(reversed(res))
        # n = len(columnNumber)
        # #ord

        # remain = 0
        # result = 0

        # for i in range(columnNumber):
        #     curr = ord(columnNumber[i]) - ord("A") + 1
        #     if remain > 0:
        #         result = curr * remain
        #     else:
        #         result = curr
        #     remain = result * 26
        
        # return result