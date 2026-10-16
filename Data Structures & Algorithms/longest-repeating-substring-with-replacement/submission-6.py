class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 
        left = 0
        best = 0
        for right in range(len(s)):
            max_freq = Counter(s[left : right + 1]).most_common(1)[0][1]
            if right - left + 1 - max_freq <= k:
                best = max(best, right - left + 1)
            else:
                left += 1
        return best
