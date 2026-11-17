class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int row = board.size(), col = board[0].size();
        auto dfs = [&](auto& self, int r, int c, int i) -> bool {
            if (i == word.size()) return true; 
            else if (r<0 || r>=row || c<0 || c>=col || board[r][c] !=word[i]) return false; 
            char temp = board[r][c];
            board[r][c] = '*'; 
            bool found = (self(self, r+1, c, i+1) ||
                          self(self, r-1, c, i+1) ||
                          self(self, r, c+1, i+1) ||
                          self(self, r, c-1, i+1)); 
            board[r][c] = temp; 
            return found; 
        }; 
        for (int r = 0; r<row; r++){
            for (int c = 0; c<col; c++){
                if (dfs(dfs,r,c,0)) return true; 
            }
        }
        return false; 
    }
};