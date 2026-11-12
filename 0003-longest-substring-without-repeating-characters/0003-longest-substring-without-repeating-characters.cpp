class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> indx(128, -1);
        int left = 0;
        int ans = 0;
        unordered_set<char> st;
        for (int i =0; i<s.size(); i++){
            while (!st.empty() && st.count(s[i])){
                st.erase(s[left]);
                left++;
            }
            st.insert(s[i]);
            ans = std::max(ans, i-left+1);
        }
        return ans; 
    }
};