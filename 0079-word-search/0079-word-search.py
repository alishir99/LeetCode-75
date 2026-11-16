class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        def dfs(r, c, i):
            if i== len(word): return True 
            elif(r<0 or r>=row or c <0 or c>=col or board[r][c]!=word[i]):
                return False 
            tmp = board[r][c]
            board[r][c] = '*'
            found = (dfs(r+1,c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))
            board[r][c] = tmp
            return found 
        ans = 0
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True 
        return False 