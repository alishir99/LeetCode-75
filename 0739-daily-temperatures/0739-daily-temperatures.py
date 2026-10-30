class Solution:
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        answer = [0]*len(temp)
        stack = []
        for i, n in enumerate(temp):
            while stack and n > temp[stack[-1]]:
                j = stack.pop()
                answer[j] = i- j
            stack.append(i)
        return answer

            




