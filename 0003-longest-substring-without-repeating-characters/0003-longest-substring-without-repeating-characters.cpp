class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> indx(128, -1);
        int left = 0;
        int ans = 0;
        for (int i=0; i<s.size(); i++){
            if(indx[s[i]] >=left){
                indx[s[i]]++;
                left = indx[s[i]];
            }
            indx[s[i]] = i;
            if (ans > (i-left +1)) ans = ans;
            else ans = i-left+1;
        }
        return ans; 
    }
};