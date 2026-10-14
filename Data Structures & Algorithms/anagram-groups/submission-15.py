class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counterMap = defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for ch in s:
                counter[ord(ch) - ord("a")] += 1

            counterMap[tuple(counter)].append(s)
        
        return list(counterMap.values())