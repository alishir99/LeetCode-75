class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indx = [-1]*128
        l = 0
        longest = 0 
        win = set()
        for i in range(len(s)): 
            while win and s[i] in win: 
                win.remove(s[l])
                l +=1
            win.add(s[i])
            longest = max(longest, i-l+1)
        return longest