class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        minute = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
        queue = deque([])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        while queue and fresh > 0:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            minute += 1
        return minute if fresh == 0 else -1
    
                        
