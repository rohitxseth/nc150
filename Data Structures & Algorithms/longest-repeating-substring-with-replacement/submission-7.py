class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 
        counter = {}
        left = 0
        best = 0
        max_freq = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            max_freq = max(max_freq, counter[s[right]])
            if right - left + 1 - max_freq <= k:
                best = max(best, right - left + 1)
            else:
                left += 1
        return best
