class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev1=prev2=0
        for c in cost: 
            new = c+min(prev1,prev2)
            prev2 = prev1 
            prev1 = new
        return min(prev1, prev2)