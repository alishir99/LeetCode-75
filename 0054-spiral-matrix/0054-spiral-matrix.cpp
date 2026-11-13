class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> out;
        while (!matrix.empty()){
            out.insert(out.end(), matrix[0].begin(), matrix[0].end());
            matrix.erase(matrix.begin());
            if(matrix.empty()) break;
            int col = matrix[0].size();
            int row = matrix.size();
            vector<vector<int>> t(col, vector<int>(row));
            for(int r =0; r<row; r++){
                for (int c = 0; c<col; c++){
                    t[c][r] = matrix[r][c];
                }
            }
            reverse(t.begin(), t.end());
            matrix = move(t);
        }
        return out;
    }

};