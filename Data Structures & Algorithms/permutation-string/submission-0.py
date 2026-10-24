from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        s1_counter = Counter(s1)

        l = 0
        r = len(s1) - 1
        while r < len(s2):
            if Counter(s2[l : r + 1]) == s1_counter:
                return True
            else:
                l += 1
                r += 1
        return False
