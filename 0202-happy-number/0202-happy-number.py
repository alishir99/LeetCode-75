class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            tot = 0
            while n>0:
                d = n%10
                tot += d*d
                n = n//10
            n = tot
        if n in seen:
            return False 
        return True 
