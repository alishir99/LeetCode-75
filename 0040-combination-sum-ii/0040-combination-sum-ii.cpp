class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> out; 
        vector<int> stack; 
        sort(candidates.begin(), candidates.end()); 
        auto dfs = [&](auto& self, int i, int rem) -> void{
            if (rem<0){return;}
            if (rem == 0){
                out.push_back(stack);
                return;
            }
            else{
                for (int j=i; j<candidates.size(); j++){
                    int v = candidates[j]; 
                    if (j>i && v == candidates[j-1]) {continue;}
                    if(v>rem){break;}
                    stack.push_back(v); 
                    self(self, j+1, rem-v);
                    stack.pop_back();
                }
            }
        };
        dfs(dfs, 0, target);
        return out; 
    }
};