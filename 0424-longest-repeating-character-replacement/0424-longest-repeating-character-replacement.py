class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxf = 0
        longest = 0
        for i, c in enumerate(s): 
            freq[c] = freq.get(c, 0)+1
            maxf = max(maxf, freq[c])
            if (i-l +1) - maxf >k: 
                freq[s[l]] -=1
                l +=1 
            longest = max(longest, i-l+1)  
        return longest