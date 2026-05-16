class Solution:
    def hasDuplicate(self, nums: list[str]):
        return len(set(nums)) != len(nums)