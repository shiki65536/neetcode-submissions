class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        output = [[0]* cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                output[col][rows-row-1] = matrix[row][col]
        
        for r in range(rows):
                matrix[r] = output[r]
