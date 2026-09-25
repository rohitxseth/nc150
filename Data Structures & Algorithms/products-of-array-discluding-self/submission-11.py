class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            n = len(nums)
            result = [1] * n
            left = right = 1
            for i in range(n):
                j = n - 1 - i
                result[i] = result[i] * left
                left = left * nums[i]
                result[j] = result[j] * right
                right = right * nums[j]
            return result