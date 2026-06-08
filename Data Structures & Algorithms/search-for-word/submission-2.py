class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def backtrack(r, c, i):
            if board[r][c] != word[i]:
                return False
            
            if i == len(word) - 1:
                return True

            visited[r][c] = True

            for dr, dc in direction:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    if backtrack(nr, nc, i + 1):
                        visited[r][c] = False
                        return True

            visited[r][c] = False
            return False

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        
        return False