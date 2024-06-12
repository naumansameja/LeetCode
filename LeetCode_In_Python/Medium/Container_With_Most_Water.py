class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0
        while start < end:
            max_area = max(max_area, min(height[start], height[end])* (end-start))
            
            if height[end] < height[start]:
                end -= 1
            else:
                start += 1
        return max_area