class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> group;
        vector<vector<string>>ans;
        for(const auto& w:strs){
            string key = w; sort(key.begin(), key.end());
            group[key].push_back(w);
        }
        for(auto& [k, v]: group){
            ans.push_back(v);
        }
        return ans;
    }
};