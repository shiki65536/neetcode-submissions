class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False

        memo = {}
        used = [False] * n
        
        def backtrack(remain):
            if all(used) and remain == 0:
                return True
            if remain == 0:
                remain = target
            state = tuple(used)
            if state in memo:
                return memo[state]
            for i in range(n):
                if remain - matchsticks[i] >= 0 and not used[i]: 
                    used[i] = True
                    if backtrack(remain - matchsticks[i]):
                        return True
                    used[i] = False
            memo[state] = False
            return False

        return backtrack(target)















        # total = sum(matchsticks)
        # target = total/4
        # if total%4 != 0:
        #     return False
        # if max(matchsticks) > target:
        #     return False
        
        # sides = [0]*4
        # matchsticks.sort(reverse=True) 

        # def backtrack(i):
        #     if i == len(matchsticks):
        #         return sides[0] == sides[1] == sides[2] == sides[3] == target
        #     for j in range(len(sides)):
        #         if sides[j] + matchsticks[i] <= target:
        #             sides[j] += matchsticks[i]
        #             if backtrack(i+1):
        #                 return True
        #             sides[j] -= matchsticks[i]
                    
        #     return False

        # return backtrack(0)







        # total = sum(matchsticks)

        # if total % 4 != 0:
        #     return False

        # target = total // 4
        # sides = [0] * 4

        # matchsticks.sort(reverse=True)

        # if matchsticks[0] > target:
        #     return False

        # def backtrack(i):
        #     if i == len(matchsticks):
        #         return sides[0] == sides[1] == sides[2] == sides[3] == target

        #     for side in range(4):
        #         if sides[side] + matchsticks[i] <= target:
        #             sides[side] += matchsticks[i]

        #             if backtrack(i + 1):
        #                 return True

        #             sides[side] -= matchsticks[i]

        #     return False

        # return backtrack(0)