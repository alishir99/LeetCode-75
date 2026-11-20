class Solution {
public:
    int characterReplacement(string s, int k) {
        int freq[26] = {};
        int l =0, longest = 0, maxf = 0; 
        for (int i = 0; i<s.size();i++){
            maxf = std::max(maxf, ++freq[s[i]-'A']);
            if((i-l+1)-maxf >k) {
                freq[s[l++]-'A']--;
            }
            longest = std::max(longest, i-l+1);
        }
        return longest;
    }
};