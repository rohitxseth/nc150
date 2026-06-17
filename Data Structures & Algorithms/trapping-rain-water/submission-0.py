class Solution:
    def trap(self, height: List[int]) -> int:
        res = [0] * len(height)
        for i in range(1, len(height)):
            res[i] = max(res[i - 1], height[i - 1])

        right_max = 0
        total_area = 0
        for i in range(len(height) - 1, -1, -1):
            right_max = max(height[i], right_max)
            area = min(right_max, res[i]) - height[i]
            if area > 0:
                total_area += area
        return total_area
