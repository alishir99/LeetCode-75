class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        output = []
        stack = []
        def backtrack(start):
            output.append(stack[:])
            for i in range(start, len(nums)):
                stack.append(nums[i])
                backtrack(i+1)
                stack.pop()
        backtrack(0)
        return output 