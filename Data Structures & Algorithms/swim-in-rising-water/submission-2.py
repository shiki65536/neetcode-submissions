class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visit = {(0,0)}
        heap = [(grid[0][0], 0, 0)] #time, r, c
        max_sec = 0

        while heap:
            t, r, c = heapq.heappop(heap)
            max_sec = max(t, max_sec)

            if r == rows - 1 and c == cols - 1:
                return max_sec

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (nr,nc) in visit:
                    continue
                if 0 <= nr < rows and 0 <= nc < cols:
                    sec = grid[nr][nc]
                    heapq.heappush(heap, (sec, nr, nc))
                    visit.add((nr,nc))

        return 0

        
