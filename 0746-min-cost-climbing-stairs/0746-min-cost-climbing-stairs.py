class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        p1=p2 = 0
        for c in cost:
            p2,p1 = p1, c+min(p1,p2)
        return min(p1,p2)