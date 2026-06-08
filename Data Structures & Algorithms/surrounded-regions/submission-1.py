class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        edge = (
            [(0, c) for c in range(cols)] +
            [(rows - 1, c) for c in range(cols)] +
            [(r, 0) for r in range(1, rows - 1)] +
            [(r, cols - 1) for r in range(1, rows - 1)]
        )

        q = deque()
        visited = set()

        # 只把邊界的 O 當起點
        for r, c in edge:
            if board[r][c] == "O" and (r, c) not in visited:
                q.append((r, c))
                visited.add((r, c))
                board[r][c] = "T"   # safe

                while q:
                    cr, cc = q.popleft()
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if board[nr][nc] == "O" and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                board[nr][nc] = "T"
                                q.append((nr, nc))

        # 翻轉
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

