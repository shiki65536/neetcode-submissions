class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = cols = n
        output = []
        path = []
        seen_c = set()
        seen_d1 = set() #r-c
        seen_d2 = set() #r+c
        def draw(c):
            word = []
            for i in range(n):
                if i == c:
                    word.append("Q")
                else:
                    word.append(".")
            return "".join(word)

        def backtrack(r):
            if r == n:
                output.append(path[:])
                return

            for c in range(n):
                if c in seen_c:
                    continue
                if r-c in seen_d1:
                    continue
                if r+c in seen_d2:
                    continue
                seen_c.add(c)
                seen_d1.add(r-c)
                seen_d2.add(r+c)
                path.append(draw(c))
                backtrack(r+1)
                seen_c.remove(c)
                seen_d1.remove(r-c)
                seen_d2.remove(r+c)
                path.pop()

        
        backtrack(0)
        return output




















        # col = set()
        # posDiag = set()
        # negDiag = set()

        # res = []
        # board = [["."] * n for _ in range(n)]

        # def backtrack(r):
        #     if r == n:
        #         copy = ["".join(row) for row in board]
        #         res.append(copy)
        #         return
        
        #     for c in range(n):
        #         if c in col or (r+c) in posDiag or (r-c) in negDiag:
        #             continue
                
        #         col.add(c)
        #         posDiag.add(r+c)
        #         negDiag.add(r-c)
        #         board[r][c] = "Q"

        #         backtrack(r+1)

        #         col.remove(c)
        #         posDiag.remove(r+c)
        #         negDiag.remove(r-c)
        #         board[r][c] = "."

        # backtrack(0)
        # return res
