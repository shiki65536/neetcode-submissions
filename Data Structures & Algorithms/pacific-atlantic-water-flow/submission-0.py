class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = [(0, c) for c in range(cols)] + [(r,0) for r in range(1, rows)]
        atl = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows-1)]
        p_start =  [(0, c) for c in range(cols)] + [(r,0) for r in range(1, rows)]
        a_start = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows-1)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(source, path):
            queue = deque(source)
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr,nc) not in path:
                        if heights[nr][nc] >= heights[r][c]:
                            path.append((nr,nc))
                            queue.append((nr,nc))

        bfs(pac, p_start)
        bfs(atl, a_start)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in p_start and (r,c) in a_start:
                    res.append((r,c))

        return res
