class Solution:
    def countBits(self, n: int) -> list[int]:
        r = [0]*(n+1)
        for i in range(n+1):
            count = 0
            j = i
            while i>0:
                b = i%2
                count +=b
                i = i//2
            r[j] = count
        return r