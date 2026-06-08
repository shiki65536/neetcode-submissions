class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            if asteroids[i] < 0 and stack and stack[-1] > 0:
                alive = True
                while alive and stack and stack[-1] > 0: 
                    prev = stack.pop()
                    if prev > abs(asteroids[i]):
                        alive = False
                        stack.append(prev)
                    elif abs(asteroids[i]) == prev:
                        alive = False
                if alive:
                    stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])

        return stack