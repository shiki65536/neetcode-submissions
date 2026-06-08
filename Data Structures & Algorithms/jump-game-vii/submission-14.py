class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        n = len(s)
        farthest = 0
        if s[0] == "1" or s[n-1] == "1":
            return False

        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump + 1, n)

            for j in range(start, end):
                if j >= n:
                    continue
                if j == n-1:
                    return True
                if s[j] == "0":
                    if farthest < j:
                        farthest = j
                        q.append(j)

        return False