class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        nums = set(nums)
        max_streak = 1

        for num in nums:
            if num - 1 not in nums:
                current_streak = 1
                while num + 1 in nums:
                    current_streak += 1
                    num = num + 1
                max_streak = max(current_streak, max_streak)
        return max_streak






# 24 Sep 2026(brute force)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         max_sequence = 0
#         current_sequence = 1
#         nums = list(set(nums))
#         nums.sort()
#         for i in range(len(nums)):
#             if i > 0 and nums[i] - nums[i - 1] == 1:
#                 current_sequence += 1
#             else:
#                 current_sequence = 1
#             max_sequence = max(max_sequence, current_sequence)
#         return max_sequence
