class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        out = []
        while matrix:
            out.extend(matrix.pop(0))
            matrix[:] = list(zip(*matrix))[::-1]
        return out