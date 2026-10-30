class Solution:
    def binary_search (self, nums, start, end, target):
        if start>end:
            return -1
        mid = (start+end)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.binary_search(nums, start, mid-1, target)
        else:
            return self.binary_search(nums, mid+1, end, target )
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        ans = self.binary_search(nums, start, end, target )
        return ans