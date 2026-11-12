class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int len = nums.size();
        k = k%len;
        int n = len - k;
        vector<int> back(nums.begin()+n, nums.end());
        back.insert(back.end(), nums.begin(), nums.begin()+n);
        nums = back;
    }
};