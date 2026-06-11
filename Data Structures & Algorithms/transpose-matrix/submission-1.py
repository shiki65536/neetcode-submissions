
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])

        output = [[0] * rows for col in range(cols)]
        print(output)

        for row in range(rows):
            for col in range(cols):
                output[col][row] = matrix[row][col]
        
        return output
