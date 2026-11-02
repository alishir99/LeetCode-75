class Solution {
public:
    int singleNumber(vector<int>& nums) {
        std::unordered_map<int, int> m; 
        for (int n: nums){
            m[n]++;
        }
        for (auto& [k,v]: m){
            if (v==1){ return k;}
        }
        return -1;
    }
};