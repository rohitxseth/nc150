# 25 Sep 2026
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        length = len(nums)
        res = []
        
        for i in range(length):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, length - 1

            while left < right:
                target = - (nums[i])
                total = nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res                    