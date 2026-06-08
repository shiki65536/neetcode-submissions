class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        queue = deque(["0000"])
        count = 0
        visited = set() # why
        visited.add("0000")
        while queue:
            size = len(queue)
            
            for _ in range(size):
                lock = queue.popleft()
                if lock == target:
                    return count
                for i in range(len(lock)):
                    num = int(lock[i])
                    if num == 9:
                        num_plus = 0
                        num_minus = 8
                    elif num == 0:
                        num_plus = 1
                        num_minus = 9
                    else:
                        num_plus = num + 1
                        num_minus = num - 1
                    num_plus = str(num_plus)
                    num_minus = str(num_minus)
                    lock_plus = lock[:i] + num_plus + lock[i+1:]
                    lock_minus = lock[:i] + num_minus + lock[i+1:]
                    if lock_plus not in deadends and lock_plus not in visited:
                        queue.append(lock_plus)
                        visited.add(lock_plus)
                    if lock_minus not in deadends and lock_minus not in visited:
                        queue.append(lock_minus)
                        visited.add(lock_minus)
            count += 1
        return -1
