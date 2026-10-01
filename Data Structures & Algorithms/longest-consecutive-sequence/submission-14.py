class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        longest = 0

        for num in nums:
            current = 0
            if num - 1 not in nums:
                current += 1
                while num + 1 in nums:
                    current += 1
                    num += 1
                longest = max(current, longest)

        return longest