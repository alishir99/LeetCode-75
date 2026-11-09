class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        output = []
        stack = []
        def backtrack(nums):
            if len(stack) == len(nums):
                output.append(stack[:])
                return 
            for n in nums:
                if n in stack:
                    continue 
                
                stack.append(n)
                backtrack(nums)
                stack.pop()
        backtrack(nums)
        return output 

