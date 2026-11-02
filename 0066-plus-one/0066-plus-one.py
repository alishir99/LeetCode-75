class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        output = digits 
        for i in range (len(digits)-1, -1, -1):
            if digits[i] < 9: 
                output[i] = digits[i]+1
                return output
            else:
                output[i] = 0
        return [1]+output
        