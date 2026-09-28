class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        length = len(nums)

        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # if nums[i] > 0:
            #     break
            target = -(nums[i])
            l, r = i + 1, length - 1
            while l < r:
                total = nums[l] + nums [r]
                if target > total:
                    l += 1
                elif target < total:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
        return ans