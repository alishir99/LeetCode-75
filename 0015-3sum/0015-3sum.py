class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out =[]
        nums.sort()
        l,r = 0, len(nums)-1
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: continue 
            l, r = i+1, len(nums)-1
            while l<r: 
                s = nums[l]+nums[i]+nums[r]
                if s==0: 
                    out.append([nums[l], nums[i], nums[r]])
                    r -=1
                    l +=1
                    while l<r and nums[l] == nums[l-1]:
                        l +=1
                elif s >0: 
                    r -=1
                else: 
                    l +=1
        return out
