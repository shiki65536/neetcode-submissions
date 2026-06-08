class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r == rows - 1 and c == cols -1:
                return grid[r][c]
            if r >= rows or c >= cols:
                return float("inf")
            if (r, c) in memo:
                return memo[(r, c)]
            memo[(r, c)] = grid[r][c] + min(dfs(r+1, c), dfs(r, c+1))
            return memo[(r,c)]
        
        return dfs(0, 0)















        rows, cols = len(grid), len(grid[0])
        memo = {}

        def dfs(r, c):
            if r >= rows or c >= cols:
                return float("inf")
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            return memo[(r, c)]

        return dfs(0, 0)



        self.best = float("inf")
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c, total, visited):
            if r == rows - 1 and c == cols - 1:
                self.best = min(self.best, total)
                return

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dfs(nr, nc, total + grid[nr][nc], visited)
                    visited.remove((nr, nc))

        dfs(0, 0, grid[0][0], {(0, 0)})
        return self.best