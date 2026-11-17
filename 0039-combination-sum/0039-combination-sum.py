class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        out = []
        stack= []
        def back(i, remainder):
            if remainder == 0: 
                out.append(stack[:])
                return 
            elif remainder < 0:
                return 
            for j in range(i,len(candidates)):
                stack.append(candidates[j])
                back(j, remainder-candidates[j])
                stack.pop()

        back(0, target) 
        return out
