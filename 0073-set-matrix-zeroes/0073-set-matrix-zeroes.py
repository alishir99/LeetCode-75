class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_col = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zero_row.add(r)
                    zero_col.add(c)
        for r in zero_row:
            matrix[r] = [0]*len(matrix[0])
        for c in zero_col:
            for i in range(len(matrix)):
                matrix[i][c] = 0 