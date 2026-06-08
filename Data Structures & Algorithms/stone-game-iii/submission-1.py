class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:        
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            take = 0
            dp[i] = float("-inf")

            for x in range(3):
                if i + x >= n:
                    break

                take += stoneValue[i + x]
                dp[i] = max(dp[i], take - dp[i + x + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"

        # mine
        scores = [0]*2
        n = len(stoneValue) - 1

        #diff = choice - max <- pick smallest diff
        def calculation(i):
            diff = float("INF")
            idx = 0
            sum = 0

            for j in range(0,3):
                if i+j >= len(stoneValue) - 1:
                    break
                sum += stoneValue[i+j]
                _, enemy = max(calculation(val) for val in stoneValue[j+1:j+4])
                
                if enemy - sum < diff:
                    diff = enemy - sum
                    idx = j
            result = sum(stoneValue[i:idx+1])
            return (idx, result)
        
        start = 0
        count = 0
        while start <= n:
            i, score = calculation(start)
            count += 1
            if count%2 !=0:
                scores[0] += score
            else:
                scores[1] += score
            start = i + 1

        if scores[0] > scores[1]:
            return "Alice"
        elif scores[0] < scores[1]:
            return "Bob"
        else:
            return "tie"


                