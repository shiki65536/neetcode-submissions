class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        grids = rows * cols
        # (row , col) = grid % cols, grid // cols
        left, right = 0, grids - 1

        while left <= right:
            mid = (left+right)//2
            r, c = mid // cols, mid % cols
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

















        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // n
            c = mid % n
            val = matrix[r][c]

            if val == target:
                return True
            if val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
            