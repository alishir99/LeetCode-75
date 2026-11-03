class Solution:
    def maxArea(self, height: list[int]) -> int:
        start, end = 0, len(height)-1
        area = 0
        while start < end:
            level = min(height[start], height[end])
            area = max(area, level*(end-start))
            if height[start]<height[end]: start +=1
            else: end -=1
        return area
        
