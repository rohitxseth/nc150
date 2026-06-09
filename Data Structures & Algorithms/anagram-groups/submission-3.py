from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for s in strs:
            freq = Counter(s)
            freq_tuple = tuple(sorted(freq.items()))
            ans[freq_tuple].append(s)
        
        return list(ans.values())


