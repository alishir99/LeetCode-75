class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indx = [-1]*128
        l = 0
        longest = 0 
        for i in range(len(s)): 
            win = s[l:i]
            while win and s[i] in win: 
                l +=1
                win = s[l:i]
         
            longest = max(longest, i-l+1)
        return longest