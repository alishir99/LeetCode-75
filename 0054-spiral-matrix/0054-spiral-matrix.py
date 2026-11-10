class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        out = []
        top,bottom,left,right = 0, len(matrix)-1, 0, len(matrix[0])-1

        while top <=bottom and left <= right:
            out.extend(matrix[top][i] for i in range(left, right+1))
            top +=1
            out.extend(matrix[i][right] for i in range(top, bottom+1))
            right -=1
            if top <=bottom:
                out.extend(matrix[bottom][i] for i in range(right, left-1, -1))
                bottom -=1
            if left <=right:
                out.extend(matrix[i][left] for i in range(bottom, top-1, -1))
                left +=1
        return out

            