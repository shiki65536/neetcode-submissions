class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        seen_c = defaultdict(set)
        seen_s = defaultdict(set)

        for r in range(rows):
            seen_r = set()
            for c in range(cols):
                char = board[r][c]

                # verify cols in row
                if char in seen_r and char != ".":
                    return False
                seen_r.add(char)

                #verify rows in col
                if char in seen_c[c] and char != ".":
                    return False
                seen_c[c].add(char)

                # verify square
                key = (r//3, c//3)
                if char in seen_s[key] and char != ".":
                    return False
                seen_s[key].add(char)
        
        return True