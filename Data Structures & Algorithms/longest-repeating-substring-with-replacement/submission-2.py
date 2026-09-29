class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        for i in range(len(s)):
            other = 0
            for j in range(i, len(s)):
                if s[j] != s[i]:
                    other += 1
                if other > k:
                    break
                best = max(best, j - i + 1)
        return best
