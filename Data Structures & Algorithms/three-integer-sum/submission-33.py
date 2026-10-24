class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        #[-1, -1, 0, 1]
        ans = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            target = -(num)
            while l < r:
                total = nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans