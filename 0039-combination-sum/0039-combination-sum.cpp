class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> out; 
        vector<int> stack; 
        auto dfs = [&](auto& self, int i, int r)->void {
            if (r==0) {
                out.push_back(stack); 
                return;
            }
            else if (r <0) {return;}
            for(int j=i; j<candidates.size(); j++){
                stack.push_back(candidates[j]); 
                self(self, j, r-candidates[j]);
                stack.pop_back();
            }
        };
        dfs(dfs, 0, target);
        return out; 
    }
};