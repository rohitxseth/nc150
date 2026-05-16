class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        numset = set(nums)
        ll = len(numset)
        if l>ll:
            return True
        else:
            return False