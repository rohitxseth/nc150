from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        freqPairs = list(freq.items())
        freqPairs.sort(key = lambda x: x[1], reverse=True)

        res = []

        for i in range(k):
            res.append(freqPairs[i][0])


        return res