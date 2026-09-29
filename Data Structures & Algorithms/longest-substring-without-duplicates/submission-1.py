class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s.replace(" ", "") is None:
            return 0
        max_len = 0
        subs = set()
        for ch in s:
            if ch not in subs:
                subs.add(ch)
            else:
                max_len = max(len(subs), max_len)
                subs.clear()
                subs.add(ch)
        return max_len