class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> output;
        vector<int> st;
        int start = 0;
        function<void(int)>backtrack=[&](int start){
            output.push_back(st);
            for (int i = start; i<nums.size(); i++){
                st.push_back(nums[i]);
                backtrack(i+1);
                st.pop_back();
            }
        };
        backtrack(0);
        return output;
    }
};