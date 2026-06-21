class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        maxL = height[0]
        maxR = height[-1]
        while l < r:
            if maxL <= maxR:
                l += 1
                area += max(0, (maxL - height[l]))
                maxL = max(maxL, height[l])
            else:
                r -= 1
                area += max(0, (maxR - height[r]))
                maxR = max(maxR, height[r])
        return area
