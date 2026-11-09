class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> output;
        vector<int> stack;
        function<void()> backtrack=[&](){
            if (stack.size() == nums.size()){
                output.push_back(stack);
                return; 
            }
            for (auto& n:nums){
                if (find(stack.begin(), stack.end(),n)!=stack.end()){ continue;}
                stack.push_back(n);
                backtrack();
                stack.pop_back();
            }
        };
        backtrack();
        return output;
    }
};