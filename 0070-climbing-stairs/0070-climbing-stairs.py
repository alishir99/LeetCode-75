class Solution:
    def climbStairs(self, n: int) -> int:
        output = [1,2]
        for i in range(2,n):
            output.append(output[i-2]+output[i-1])
        return output[n-1]
