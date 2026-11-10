class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0;
        int longest = 0;
        vector<int> last(128,-1);
        for (int i=0; i<s.size(); i++){
            if (last[s[i]]>=start) start = last[s[i]]+1;
            last[s[i]] = i;
            longest = std::max(longest, i-start+1);
        }
        return longest;
    }
};