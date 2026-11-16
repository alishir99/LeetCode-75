class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)+1
        tot = (n*(n-1))//2

        return tot-sum(nums)


