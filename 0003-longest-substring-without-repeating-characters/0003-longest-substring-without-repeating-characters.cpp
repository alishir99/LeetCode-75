class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0;
        int ans = 0;
        vector<int> last(128, -1);
        unordered_set<char> st;
        for (int i=0; i<s.size(); i++){
            if(last[s[i]]>=start){
                start = last[s[i]]+1;
            }
            last[s[i]] = i;
            ans = std::max(ans, i-start+1);
        }
        return ans;
    }
};