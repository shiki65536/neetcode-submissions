class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visit = set() #(r,c)
        heap = [(0,0,0)]

        while heap:
            diff, r, c = heapq.heappop(heap)

            if (r, c) in visit:
                continue
            visit.add((r,c))
            if (r, c) == (rows-1, cols-1):
                return diff

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if not 0 <= nr < rows or not 0 <= nc < cols or (nr,nc) in visit:
                    continue
                
                new_diff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(heap,[new_diff, nr, nc])

        return 0           
                    





        ## mine
        rows, cols = len(heights), len(heights[0])
        cache = {} #(r1,c1,r2,c2): diff
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set((0,0)) #(r,c)
        min_max_diff = float("inf")

        def backtrack(r, c, max_diff):
            nonlocal min_max_diff
            if r == rows-1 and c == cols-1:
                min_max_diff = min(max_diff, min_max_diff)
                return
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if  0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if (r,c,nr,nc) in cache:
                            new_diff = cache[(r,c,nr,nc)]
                        else:
                            new_diff = abs(heights[r][c]-heights[nr][nc])
                            cache[(r,c,nr,nc)] = new_diff

                        backtrack(nr, nc, max(new_diff, max_diff))
                        visited.remove((nr, nc))

        backtrack(0, 0, 0)
        return min_max_diff