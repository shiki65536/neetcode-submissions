class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        q = deque([0])
        visited = set([0])
        jumps = 0

        while q:
            size = len(q)
            for _ in range(size):
                idx = q.popleft()
                far = idx + nums[idx]
                if far >= n - 1:
                    return jumps + 1

                for nxt in range(idx + 1, far + 1):
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            jumps += 1

        return jumps