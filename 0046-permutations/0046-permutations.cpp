class Solution {
public:
    void backtrack(vector<int>& path, vector<int>& nums, vector<vector<int>>& result){
        if (path.size()==nums.size()){
            result.push_back(path);
            return;
        }
        for(auto n: nums){
            if(find(path.begin(), path.end(), n)!= path.end()){continue;}
            path.push_back(n);
            backtrack(path, nums, result);
            path.pop_back();
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> path;
        backtrack(path, nums, result);
        return result; 
    }
};