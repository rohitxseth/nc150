class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            freq_tuple = tuple(freq)
            freqMap[freq_tuple].append(s)

        return list(freqMap.values())