class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
         
        for i in range(len(nums) - k):
            j = i + k
            if nums[i] == nums[j]:
                return True
        return False