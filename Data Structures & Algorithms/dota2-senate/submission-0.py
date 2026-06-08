class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(list(senate))
        r = 0
        d = 0

        while q:
            size = len(q)
            for _ in range(size):
                s = q.popleft()
                if s == "R":
                    if r > 0:
                        r -= 1
                    else:
                        d += 1
                        q.append(s)
                else:
                    if d > 0:
                        d -= 1
                    else:
                        r += 1
                        q.append(s)
            if len(q) == size:
                return "Radiant" if q[0] == "R" else "Dire"
            
                
