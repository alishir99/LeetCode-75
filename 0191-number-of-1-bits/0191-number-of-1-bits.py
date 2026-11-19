class Solution:
    def hammingWeight(self, n: int) -> int:
        b= 0
        while n>0: 
            b += n&1
            n//=2
        return b 
