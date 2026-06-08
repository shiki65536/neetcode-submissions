class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        count = 0
        while count <= n:
            res.append(bin(count).count("1"))
            count +=1

        return res

        