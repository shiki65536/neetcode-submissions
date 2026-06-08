class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        r_visited = set()
        c_visited = set()
        s_visited = set()
        

        for row in range(rows):
            for col in range(cols):
                digit = board[row][col]
                sub = (row // 3, col // 3)
                if digit == ".":
                    continue
                else:
                    if (row, digit) in r_visited or (col, digit) in c_visited or (sub, digit) in s_visited:
                        return False
                    else:
                        r_visited.add((row, digit))
                        c_visited.add((col, digit))
                        s_visited.add((sub, digit))


        return True
















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