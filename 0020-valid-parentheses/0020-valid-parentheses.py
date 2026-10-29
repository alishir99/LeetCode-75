class Solution:
    def isValid(self, s: str) -> bool:
        left = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for i in s:
            if i in "(, [, {": 
                stack.append(i)
            elif stack and left[i] is stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack)==0