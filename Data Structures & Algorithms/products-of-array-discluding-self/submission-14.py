class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        ans = [1] * length

        prefix = 1
        suffix = 1
        for left in range(length):
            right = length - 1 - left
            ans[left] *= prefix 
            ans[right] *= suffix 
            prefix *= nums[left]
            suffix *= nums[right]
        
        return ans