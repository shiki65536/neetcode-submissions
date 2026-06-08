class Solution:
    def reverseBits(self, n: int) -> int:
        # binary = format(n, "032b")
        # return int(binary[::-1], 2)
        res = 0

        for i in range(32):
            bit = n & 1
            res = (res << 1) | bit
            n >>= 1

        return res