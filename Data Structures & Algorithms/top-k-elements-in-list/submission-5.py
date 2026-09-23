#23 sept 2026
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = {}
        for num in nums:
            freq_counter[num] = freq_counter.get(num, 0) + 1


        index_list =[[] for _ in range(len(nums) + 1)]

        for num, index in freq_counter.items():
            index_list[index].append(num)

        ans = []
        for i in index_list[::-1]:
            for j in i:
                ans.append(j)
                if len(ans) == k:
                    return ans
