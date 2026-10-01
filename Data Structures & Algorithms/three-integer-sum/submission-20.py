class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if nums[i] == nums[i - 1]:
                continue
            target = -(nums[i])
            left, right = i, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > right:
                    right -= 1
                elif total == target:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while right < left and nums[right - 1] == nums[right]:
                        right -= 1
                left += 1
                right -= 1
        return res