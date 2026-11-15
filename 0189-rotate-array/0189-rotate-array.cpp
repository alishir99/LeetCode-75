class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = k%nums.size(); 
        int n = nums.size()-k;
        vector<int> res(nums.size());
        for (int i = 0; i<nums.size(); i++){
            res[(i+k)%nums.size()] = nums[i]; 
        }
        nums = move(res);
    }
};