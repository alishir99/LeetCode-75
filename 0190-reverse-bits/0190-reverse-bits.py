class Solution:
    def reverseBits(self, n: int) -> int:
        b = ''
        while len(b)!=32:
            b = b+str(n&1)
            n = n//2
        return int(b, 2)