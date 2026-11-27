class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        out = [] 
        stack = [] 
        candidates.sort()
        def dfs(i,  rem): 
            if rem <0: 
                return 
            if rem ==0: 
                out.append(stack[:])
                return 
            else: 
                for j in range(i, len(candidates)):
                    if j>i and candidates[j] == candidates[j-1]: continue  
                    stack.append(candidates[j])
                    dfs(j+1, rem-candidates[j])
                    stack.pop()
        
        dfs(0, target)
        return out