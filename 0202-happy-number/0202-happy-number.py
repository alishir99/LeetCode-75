class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def next(x):
            r = 0
            while x>0:
                d = x%10
                r +=d*d
                x = x//10
            return r
        while n!=1 and n not in seen:
            seen.add(n)
            n = next(n)
        return True if n==1 else False 
        
