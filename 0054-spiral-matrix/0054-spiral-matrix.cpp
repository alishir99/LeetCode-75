class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {

        vector<int> out;
        while (!matrix.empty()){
            out.insert(out.end(), matrix[0].begin(), matrix[0].end());
            matrix.erase(matrix.begin());
            if (matrix.empty()) break;
            int row = matrix.size();
            int col = matrix[0].size();
            vector<vector<int>> t(col, vector<int>(row));
            for (int i = 0; i<row; i++){
                for (int j=0; j<col; j++){
                    t[j][i] = matrix[i][j];
                }
            }
            reverse(t.begin(), t.end());
            matrix = move(t);
        }
        return out;
    }
};