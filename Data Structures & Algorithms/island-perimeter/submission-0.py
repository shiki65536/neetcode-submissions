class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(0,-1), (1,0), (-1,0)]

        def dfs(r, c):
            line = 0
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not 0 <= nr < rows or not 0 <= nc < cols:
                    line += 1
                elif grid[nr][nc] == 0:
                    line += 1

            return line


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    perimeter += dfs(row, col)
        
        return perimeter