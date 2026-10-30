class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []

        def backtrack ( open_num, close_num):
            if len(stack)== 2*n:
                res.append("".join(stack))
                return 
            if open_num <n:
                stack.append('(')
                backtrack(open_num+1, close_num)
                stack.pop()
            if close_num < open_num:
                stack.append(')')
                backtrack(open_num, close_num+1)
                stack.pop()
        backtrack(0,0)
        return res
