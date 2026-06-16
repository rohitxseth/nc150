class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0 , len(heights) - 1
        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            area = h * w
            max_area = max(area, max_area)
            if h == heights[l]:
                l += 1
            else:
                r -= 1
        return max_area
            