class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            if (i>0 and nums[i]==nums[i-1]): continue 
            while l < r :
                tot = nums[i]+nums[l]+nums[r]
                if tot==0:
                    result.append([nums[i], nums[l], nums[r]])
                    l +=1
                    r -=1
                    while l < r and nums[l]==nums[l-1]: l +=1 
                elif tot>0: r -=1
                else: l +=1
        return result 

