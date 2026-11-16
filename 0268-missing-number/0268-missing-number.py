class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        tot = 0
        for i in range(len(nums)+1):
            tot +=i
        return tot-sum(nums)


