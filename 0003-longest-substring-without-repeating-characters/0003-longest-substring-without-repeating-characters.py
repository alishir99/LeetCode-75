class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0 
        for i in range(len(s)):
            window = s[left:i]
            while s[i] in window:
                left +=1
                window = s[left:i]
            ans = max(ans, i-left+1)
        return ans
        