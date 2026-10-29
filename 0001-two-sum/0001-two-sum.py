class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in seen:
                seen[n] = i
            else: 
                return [seen[diff], i]         