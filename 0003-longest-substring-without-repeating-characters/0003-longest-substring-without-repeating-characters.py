class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        ans = 0
        window = set()
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[start])
                start +=1
            window.add(s[i])
            ans = max(ans, i-start+1)
            
        return ans