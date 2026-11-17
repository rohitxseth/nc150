class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        even = 0
        odd = len(nums) - 1

        for num in nums:
            if num % 2 == 0:
                ans[even] = num
                even += 1
            else:
                ans[odd] = num
                odd -= 1
        
        return ans