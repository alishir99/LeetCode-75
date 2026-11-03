class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result; 
        int l = 0;
        int r = 0; 
        for (int i = 0; i<size(nums); i++){
            l= i+1;
            r= nums.size()-1; 
            if (i>0 && nums[i]==nums[i-1]){continue;}
            while (l < r){
                int tot = nums[i]+nums[l]+nums[r];
                if (tot == 0){
                    result.push_back({nums[i], nums[l],nums[r]});
                    l++;
                    r--;
                    while(l<r && nums[l]==nums[l-1]) l++; 
                }
                else if (tot>0){r--;}
                else{l++;} 
                 
            }
        }
        return result;
    }
};