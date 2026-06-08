class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        def counter(num):
            count = 0
            while num:
                num &= (num-1)
                count += 1
            return count

        for num in range(n+1):
            output.append(counter(num))
        
        return output

        # 2








        # res = []
        # count = 0
        # while count <= n:
        #     res.append(bin(count).count("1"))
        #     count +=1

        # return res

        