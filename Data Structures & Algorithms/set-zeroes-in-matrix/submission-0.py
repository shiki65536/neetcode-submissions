class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        copy = [row[:] for row in matrix]
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c, dr, dc):
            nr, nc = r+dr, c+dc
            if not 0 <= nr < rows or not 0 <= nc < cols:
                return
            matrix[nr][nc] = 0
            dfs(nr, nc, dr, dc)

        for row in range(rows):
            for col in range(cols):
                if copy[row][col] != 0:
                    continue
                for (dr, dc) in directions:
                    dfs(row, col, dr, dc)
    