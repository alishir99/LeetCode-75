class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        vector<vector<int>>out(nums.size()+1);
        for (int i: nums){
            freq[i]++; 
        }
        for(auto& [num, count]:freq){
            out[count].push_back(num);
        }
        vector<int> res;
        for (int i = out.size()-1; i>=0; i--){
            for (auto j:out[i]){
                res.push_back(j);
                if(res.size()==k){return res;}
            }
        }
        return res;
    }
};