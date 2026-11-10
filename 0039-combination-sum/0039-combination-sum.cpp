class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> output;
        vector<int>st;
        int remain = 0; 
        int start = 0; 
        function<void(int, int)> backtrack = [&](int start, int remain){
            if (remain == 0) {output.push_back(st); return;}
            if(remain<0){return;}
            for(int i=start; i<candidates.size(); i++){
                st.push_back(candidates[i]);
                backtrack(i, remain-candidates[i]);
                st.pop_back();
            }
        };
        backtrack(0, target);
        return output; 
    }
};