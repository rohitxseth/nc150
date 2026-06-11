class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n: int = len(nums)
        res: List[int] = []
        leftProducts: List[int] = [1] * n
        rightProducts: List[int] = [1] * n

        for i in range(1,n,1):
            leftProducts[i] = leftProducts[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            rightProducts[i] = rightProducts[i+1]*nums[i+1]
        for i in range(n):
            res.append(leftProducts[i]*rightProducts[i])
        
        return res

