class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        out= [0]*2*n
        for i in range(2*n): 
            if i>=len(nums): 
                out[i] = nums[i%n]
            else: 
                out[i]= nums[i]
        return out 