class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        q = deque([])

        total = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    total += 1
        count = 0
        
        while q and total:
            count += 1
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if not 0 <= nr < rows or not 0 <= nc < cols:
                        continue
                    if grid[nr][nc] == 1:
                        total -= 1
                        q.append((nr, nc))
                        grid[nr][nc] = 0

        return count if total == 0 else -1

















        # rows, cols = len(grid), len(grid[0])
        # fresh = 0
        # queue = deque([])

        # # initialize fresh and rotten
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == 1:
        #             fresh += 1
        #         elif grid[row][col] == 2:
        #             queue.append((row, col))
        
        # # rotten spreading
        # directions = ((1,0),(-1,0),(0,1),(0,-1))
        # count = 0

        # while queue and fresh > 0:
        #     size = len(queue)
        #     for _ in range(size):
        #         r, c = queue.popleft()
        #         for dr, dc in directions:
        #             nr, nc = r+dr, c+dc
        #             if 0<= nr < rows and 0 <= nc < cols:
        #                 if grid[nr][nc] == 1:
        #                     queue.append((nr, nc))
        #                     fresh -= 1
        #                     grid[nr][nc] = 2
        #     count += 1
        
        # return count if fresh == 0 else -1




















        # # rows, cols = len(grid), len(grid[0])
        # # fresh = 0
        # # minute = 0
        # # directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
        # # queue = deque([])

        # # for row in range(rows):
        # #     for col in range(cols):
        # #         if grid[row][col] == 2:
        # #             queue.append((row,col))
        # #         elif grid[row][col] == 1:
        # #             fresh += 1
        
        # # while queue and fresh > 0:
        # #     size = len(queue)
        # #     for _ in range(size):
        # #         r, c = queue.popleft()
        # #         for dr, dc in directions:
        # #             nr, nc = r+dr, c+dc
        # #             if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
        # #                 fresh -= 1
        # #                 grid[nr][nc] = 2
        # #                 queue.append((nr, nc))
        # #     minute += 1
        # # return minute if fresh == 0 else -1
    
                        
