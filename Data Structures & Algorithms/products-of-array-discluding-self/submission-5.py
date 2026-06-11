class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n:int = len(nums)
        res: List[int] = [1]*n
        prefix: int = 1

        for i in range(n-2, -1, -1):
            res[i] = res[i+1]*nums[i+1]

        for i in range(1, n):
            prefix = prefix*nums[i-1]
            res[i] *= prefix
            
        return res