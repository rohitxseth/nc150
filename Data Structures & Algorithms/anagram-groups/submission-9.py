class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")] += 1
            count_tuple = tuple(count)
            res[count_tuple].append(s)
        
        return list(res.values())