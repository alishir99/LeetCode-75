class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            n = (right-left)//2
            i = left+n
            if target == nums[i]:
                return i
            elif target > nums[i]:
                left = i +1
            elif target < nums[i]:
                right = i-1
        return -1
