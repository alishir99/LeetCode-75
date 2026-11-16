class Solution {

public:
    bool exist(vector<vector<char>>& board, string word) {
        int row = board.size();
        int col = board[0].size();
        function<bool(int, int, int)>dfs = [&](int r, int c, int i){
            if (i==word.size()) return true;
            else if (r<0 || r>=row || c<0 || c>=col || board[r][c]!=word[i]) return false;
            char tmp = board[r][c];
            board[r][c] = '*';
            bool found = (dfs(r+1, c, i+1)||
                     dfs(r-1, c, i+1)||
                     dfs(r, c+1, i+1)||
                     dfs(r, c-1, i+1));
            board[r][c] = tmp;
            return found;
        };
        for(auto r = 0; r<row; r++){
            for (auto c = 0; c<col; c++){
                if(dfs(r,c,0)) return true; 
            }
        }
        return false; 
    }
};