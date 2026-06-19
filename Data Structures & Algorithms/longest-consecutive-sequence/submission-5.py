class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums = set(nums)
        max_streak = 0

        for num in nums:
            if num - 1 not in nums:
                streak = 1
                while num + 1 in nums:
                    streak += 1
                    num += 1
                max_streak = max(max_streak, streak)
        
        return max_streak