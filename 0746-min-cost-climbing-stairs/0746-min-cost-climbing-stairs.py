class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        first = sec = 0
        for c in cost:
            sec, first = first , c+min(first, sec)

        return min(first, sec)