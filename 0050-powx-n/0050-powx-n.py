class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0: 
            return 1/self.myPow(x, -n)
        if n == 0: return 1
        half = self.myPow(x, n//2)
        return half*half if n%2==0 else half*half*x