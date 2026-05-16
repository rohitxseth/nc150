# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s, key=str.lower) == sorted(t, key=str.lower)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        scount = {}
        tcount = {}
        for x in s:
            scount[x] = scount.get(x,0)+1
        for x in t:
            tcount[x] = tcount.get(x,0)+1
        return scount == tcount
