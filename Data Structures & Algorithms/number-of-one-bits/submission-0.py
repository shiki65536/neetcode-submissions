class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n &= (n-1)
            count += 1
        
        return count



















        # count = 0
        # print(n)
        # while n:
        #     n &= (n - 1)
        #     print(n)
        #     count += 1
                
        # return count