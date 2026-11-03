class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        num_set = set(nums)
        is_consecutive = (len(num_set) == len(nums)) and (max(num_set) - min(num_set) == len(nums) - 1)