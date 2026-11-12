class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        unordered_set<int> zero_row;
        unordered_set<int> zero_col;
        for (int r =0; r<matrix.size(); r++){
            for (int c = 0; c<matrix[0].size(); c++){
                if( matrix[r][c] ==0){
                    zero_row.insert(r);
                    zero_col.insert(c);
                }
            }
        }
        for (auto& r: zero_row){
            std::fill(matrix[r].begin(), matrix[r].end(), 0);
        }
        for(auto& c: zero_col){
            for (auto &r: matrix){
                r[c] = 0;
            }
        }
    }
};