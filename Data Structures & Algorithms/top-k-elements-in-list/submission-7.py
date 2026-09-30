class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}

        for i, num in enumerate(nums):
            counter[num] = counter.get(num, 0) + 1
        
        return sorted(counter, key = counter.get, reverse = True)[:k]

        