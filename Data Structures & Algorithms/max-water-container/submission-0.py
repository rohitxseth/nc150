class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                h = min(heights[i], heights[j])
                l = abs(i-j)
                area = h * l
                max_area  = max(max_area, area)
        return max_area