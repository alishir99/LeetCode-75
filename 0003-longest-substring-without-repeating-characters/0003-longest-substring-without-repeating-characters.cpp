class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0;
        int longest = 0;
        unordered_set<char> seen;
        for (int i=0; i<s.size(); i++){
            while (seen.count(s[i])){
                seen.erase(s[start]);
                start++; 
            }
            seen.insert(s[i]);
            longest = std::max(longest, i+1-start);
        }
        return longest;
    }
};