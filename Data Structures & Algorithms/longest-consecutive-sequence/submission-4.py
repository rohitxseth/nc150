class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        nums = set(nums)
        max_streak = 0

        for num in nums:
            if num - 1 not in nums:
                current_streak = 1
                while num + 1 in nums:
                    current_streak += 1
                    num += 1
                max_streak = max(max_streak, current_streak)
        return max_streak
        