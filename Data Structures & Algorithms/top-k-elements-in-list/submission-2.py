#revision
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        freq = list(freq_dict.keys())
        freq.sort()
        return freq[-1:-k-1:-1]