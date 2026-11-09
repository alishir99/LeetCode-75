class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0;
        int ans = 0;
        unordered_set<char> st;
        for (int i=0; i<s.size(); i++){
             while (st.count(s[i])){
                st.erase(s[start]);
                start ++;
            }
            st.insert(s[i]);
            ans = std::max(ans, i-start+1);
        }
        return ans;
    }
};