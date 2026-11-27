class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out =set()
        nums.sort()
        l,r = 0, len(nums)-1
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l<r: 
                s = nums[l]+nums[i]+nums[r]
                if s==0: 
                    out.add((nums[l], nums[i], nums[r]))
                    r -=1
                    l +=1
                elif s >0: 
                    r -=1
                else: 
                    l +=1
        return [list(t) for t in out]
