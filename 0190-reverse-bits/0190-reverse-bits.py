class Solution:
    def reverseBits(self, n: int) -> int:
        ans = ''
        r = 0
        for _ in range(32): 
            b = n%2
            ans = ans+str(b)
            n//=2
        power = len(ans)-1
        for i in ans: 
            if i =='1': 
                r +=2**power
            power -=1
        return r