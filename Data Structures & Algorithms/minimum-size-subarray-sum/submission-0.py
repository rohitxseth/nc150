class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_len = float("inf")
        l = 0
        total = nums[0]

        for r in range(len(nums)):
            if total >= target:
                min_len = min(min_len, r - l)
                l += 1
                total -= nums[l]
            else:
                total += nums[r]
        
        return 0 if min_len == float("inf") else min_len