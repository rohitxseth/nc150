#revision
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l

        for i in range(l - 1):
            res[i + 1] = res[i] * nums[i]
            
        suffix = 1
        for i in range(l - 2, -1, -1):
            suffix = suffix * nums[i + 1]
            res[i] *= suffix
        return res 
            