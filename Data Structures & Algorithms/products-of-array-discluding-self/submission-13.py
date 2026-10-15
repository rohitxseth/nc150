class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        l = len(nums)
        ans = [1] * l

        # [1, 1, 2, 8]
        prefix = 1
        for i in range(l):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(l - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans