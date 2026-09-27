# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:

#         nums_set = set(nums)
#         longest_sequence = 0

#         for num in nums:
#             if num - 1 not in nums:
#                 sequence = 1
#                 while num + 1 in nums:
#                     sequence += 1
#                     num += 1
#                 longest_sequence = max(sequence, longest_sequence)
        
#         return longest_sequence


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        longest_sequence = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                sequence = 1
                while num + 1 in nums_set:
                    sequence += 1
                    num += 1
                longest_sequence = max(sequence, longest_sequence)
        
        return longest_sequence