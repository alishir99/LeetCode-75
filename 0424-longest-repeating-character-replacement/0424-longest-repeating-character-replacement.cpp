class Solution {
public:
    int characterReplacement(string s, int k) {
        int l= 0, ans = 0, maxf =0; 
        int freq[26] = {};
        for (int i = 0; i<s.size(); i++){
            maxf = std::max(maxf, ++freq[s[i]-'A']); 
            if ((i-l +1)- maxf >k) {
                freq[s[l++]-'A'] --; 
            }
            ans = std::max(ans, i-l+1);
        }
        return ans; 
    }
};