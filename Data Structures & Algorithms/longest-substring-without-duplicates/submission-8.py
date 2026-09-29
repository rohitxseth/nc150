class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        l, best = 0, 0
        for r, ch in enumerate(s):
            if ch in charMap:
                l = charMap[ch] + 1
            charMap[ch] = r
            best = max(best, r - l + 1)
        return best