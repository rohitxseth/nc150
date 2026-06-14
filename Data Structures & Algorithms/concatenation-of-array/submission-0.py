class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []*len(nums)*2
        res.extend(nums)
        res.extend(nums)
        return res
        