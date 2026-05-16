# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] + nums[j] == target:
#                     ans = [i,j]
#                     ans.sort()
#                     return ans

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffdict = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if nums[i] in diffdict:
                j = diffdict.get(nums[i])
                ans = [i,j]
                ans.sort()
                return ans
            else:
                diffdict[diff] = i

