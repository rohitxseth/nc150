class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res: List[int] = []

        for i in nums:
            product: int = 1
            for j in nums:
                if j != i:
                    product *= j
            res.append(product)
        
        return res
            
