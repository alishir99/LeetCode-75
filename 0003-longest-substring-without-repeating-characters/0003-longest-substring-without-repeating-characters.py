class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1]*128
        l = 0
        longest = 0
        for i,c in enumerate(s):
            if last[ord(c)]>=l:
                l = last[ord(c)]+1
            last[ord(c)] = i
            longest = max(longest, i-l+1)
        return longest