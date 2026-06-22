# revision
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0
        l, r = 1, n - 2
        area = 0
        maxL, maxR = height[0], height[n - 1]
        while l <= r:
            if maxL < maxR:
                area += max(0, (maxL - height[l]))
                maxL = max(maxL, height[l])
                l += 1
            else:
                area += max(0, (maxR - height[r]))
                maxR = max(maxR, height[r])
                r -= 1
        return area
            