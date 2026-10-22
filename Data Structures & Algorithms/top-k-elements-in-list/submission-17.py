class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        # 1 - 1, 2 -2, 3 - 3

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counter.items():
            buckets[count].append(num)
        # [[1],[2],[3]]

        ans = []

        for bucket in reversed(buckets):
            for i in bucket:
                if k > 0:
                    ans.append(i)
                    k -= 1
        
        return ans