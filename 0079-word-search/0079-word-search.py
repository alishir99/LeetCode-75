class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        def back(r, c, i): 
            if i == len(word): return True 
            elif (r<0 or r>=row or c<0 or c>=col or board[r][c]!=word[i]): 
                return False 
            temp = board[r][c]
            board[r][c] = '*' # viisited 
            found = (back(r+1, c, i+1) or
                     back(r-1, c, i+1) or
                     back(r, c+1, i+1) or 
                     back(r, c-1, i+1) )
            board[r][c] = temp
            return found  
        for r in range(row):
            for c in range(col):
                if back(r,c,0): return True 
        return False 