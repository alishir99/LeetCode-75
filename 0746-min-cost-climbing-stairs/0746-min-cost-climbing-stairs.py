class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev1=prev2=0
        for c in cost: 
            prev2,prev1 =prev1, c+min(prev1,prev2)
        return min(prev1, prev2)