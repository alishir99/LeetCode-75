class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ''
        for chars in zip(*strs): 
            if len(set(chars))!=1: break
            ans +=chars[0]
        return ans