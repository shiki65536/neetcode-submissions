class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        output = []
        seen = set()

        def dfs(r,c,count):
            seen.add((r,c))
            output.append(matrix[r][c])
            if len(seen) == rows*cols:
                return
            mr, mc = directions[count%4]
            if (r+mr, c+mc) in seen or not 0 <= r+mr < rows or not 0 <= c+mc < cols:
                count += 1
                mr, mc = directions[count%4]
            dfs(r+mr, c+mc, count)
        
        dfs(0,0,0)
        return output