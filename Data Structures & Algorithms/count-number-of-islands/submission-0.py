class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        direction = [(1,0),(-1,0),(0,-1),(0,1)]

        def bfs(r, c):
            grid[r][c] = "0"
            for dr, dc in direction:
                nr, nc = r+dr, c+dc
                if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == "1":
                    bfs(nr, nc)
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != "0":
                    count += 1
                    bfs(row, col)
        
        return count