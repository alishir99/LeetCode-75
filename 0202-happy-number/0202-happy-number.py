class Solution:
    def isHappy(self, n: int) -> bool:

        def next_num(n):
            tot = 0
            while n>0:
                d = n%10
                tot += d*d
                n = n//10
            return tot
        slow = n
        fast = next_num(n)
        while slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        return fast==1
