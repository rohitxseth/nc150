#revision
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq_dict = Counter(nums)
#         freq = list(freq_dict.items())
#         freq.sort(key = lambda x: x[1], reverse = True)
#         res = []
#         for i in range(k):
#             res.append(freq[i][0])
#         return res