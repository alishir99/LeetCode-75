class Solution:
    def climbStairs(self, n: int) -> int:
        output = [1,2]
        for i in range(2,n):
            output.append(output[i-1]+output[i-2])
        return output[-1] if n> 1 else 1