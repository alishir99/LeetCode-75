class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ans=0
        for i, n in enumerate(nums):
            ans ^=i^n
        return ans^len(nums)




