class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans =0
        left = 0
        seen = set()
        for i in range(len(s)):
            while seen and s[i] in seen:
                seen.remove(s[left])
                left +=1

            seen.add(s[i])
            ans = max(ans, i-left+1)
        return ans