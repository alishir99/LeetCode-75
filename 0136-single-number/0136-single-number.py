class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single= {}
        for i in nums:
            single[i] = single.get(i, 0)+1
        for i in nums:
            if single[i]==1:
                return i
        