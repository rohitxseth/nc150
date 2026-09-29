class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        subs = set()
        left = 0
        for right in range(len(s)):
            if s[right] in subs:
                max_len = max(len(subs), max_len)
                left = s.find(s[right], left)
                subs.clear()
                subs.update(s[left : right + 1])
            else:
                subs.add(s[right])
        return max_len