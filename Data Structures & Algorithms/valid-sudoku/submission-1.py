class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        # check rows
        for r in range(rows):
            digits = set()
            for c in range(cols):
                v = board[r][c]
                if v == ".":
                    continue
                if v in digits:
                    return False
                digits.add(v)

        # check cols
        for c in range(cols):
            digits = set()
            for r in range(rows):
                v = board[r][c]
                if v == ".":
                    continue
                if v in digits:
                    return False
                digits.add(v)

        # check sub-boxes
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                digits = set()
                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):
                        v = board[r][c]
                        if v == ".":
                            continue
                        if v in digits:
                            return False
                        digits.add(v)

        return True
