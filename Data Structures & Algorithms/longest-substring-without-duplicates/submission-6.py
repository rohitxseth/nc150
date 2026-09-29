class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = best = 0
        for r, ch in enumerate(s):
            while ch in window:
                window.remove(s[l])
                l += 1
            window.add(ch)
            best = max(best, r - l + 1)
        return best