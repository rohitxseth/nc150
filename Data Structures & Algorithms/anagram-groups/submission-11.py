#revision
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            freq_tuple = tuple(freq)
            freq_dict[freq_tuple].append(s)
        return [s for s in freq_dict.values()]
