class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0]*2
        
        for bill in bills:
            if bill == 5:
                change[0] += 5
            elif bill == 10:
                if change[0] == 0:
                    return False
                change[1] += 10
                change[0] -= 5
            elif bill == 20:
                if sum(change) < 15 or change[0] < 5:
                    return False
                if change[1] >= 10:
                    change[1] -= 10
                    change[0] -= 5
                else:
                    change[0] -= 15
        
        return True
