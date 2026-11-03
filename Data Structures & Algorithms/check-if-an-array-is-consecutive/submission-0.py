class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        nums.sort()

        if (nums[-1] - nums[0])  == len(nums) - 1:
            return True
        return False
                