class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remain = 1

        for i in range(len(digits)-1, -1, -1):
            num = remain + digits[i]
            digit = num%10
            remain = num//10
            digits[i] = digit
        
        if remain:
            digits = [remain] + digits
        return digits