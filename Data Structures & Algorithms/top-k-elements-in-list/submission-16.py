class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counter.items():
            buckets[count].append(num)

        ans = []

        for bucket in buckets:
            for i in bucket:
                while k:
                    ans.append(bucket[i])
        
        return ans