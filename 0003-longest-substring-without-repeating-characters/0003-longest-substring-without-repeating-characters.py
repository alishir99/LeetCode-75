class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indx = [-1]*128
        l = 0
        longest = 0 
        for i in range(len(s)): 
            if indx[ord(s[i])] >=l: 
                l = indx[ord(s[i])]+1
            indx[ord(s[i])] = i 
            longest = max(longest, i-l+1)
        return longest