class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        indx = [-1]*128
        for i in range(len(s)):
            if indx[ord(s[i])]>=left:
                indx[ord(s[i])] +=1
                left = indx[ord(s[i])]
            indx[ord(s[i])] = i
            ans = max(ans, i-left+1)
        return ans
    