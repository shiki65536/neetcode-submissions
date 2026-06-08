class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(row, col):
            q = deque([(row,col)])
            visited = set()
            count = 0

            while q:
                size = len(q)
                for _ in range(size):
                    r, c = q.popleft()
                    visited.add((r, c))
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if (0 <= nr < rows) and (0 <= nc < cols) and (nr,nc) not in visited:
                            if grid[nr][nc] == -1:
                                continue
                            if grid[nr][nc] == 0:
                                return count + 1
                            q.append((nr, nc))
                            
                count += 1


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != -1 and  grid[row][col] != 0:
                    dist = bfs(row, col)
                    grid[row][col] = dist
        
