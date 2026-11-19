class Solution {
public:
    int characterReplacement(string s, int k) {
        int l= 0, ans = 0, maxf =0; 
        unordered_map<char, int> freq; 
        for (int i = 0; i<s.size(); i++){
            if (freq[s[i]] ==0) freq[s[i]] = 1; 
            else freq[s[i]] ++; 
            maxf = std::max(maxf, freq[s[i]]); 
            if ((i-l +1)- maxf >k) {
                freq[s[l]] --; 
                l++;
            }
            ans = std::max(ans, i-l+1);
        }
        return ans; 
    }
};