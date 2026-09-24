class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence = 0
        current_sequence = 1
        nums = list(set(nums))
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] - nums[i - 1] == 1:
                current_sequence += 1
            max_sequence = max(max_sequence, current_sequence)
        return max_sequence
