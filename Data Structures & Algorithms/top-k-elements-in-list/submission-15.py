class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}

        for i, num in enumerate(nums):
            counter[num] = counter.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counter.items():
            buckets[count].append(num)
        
        ans = []
        
        for bucket in reversed(buckets):
            for num in bucket:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans
        