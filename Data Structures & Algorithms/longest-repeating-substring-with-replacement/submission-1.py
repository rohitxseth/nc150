class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        for i in range(len(s)):
            cur = 0
            other = 0
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    cur += 1
                else:
                    if other < k:
                        cur += 1
                        other += 1
                    else: break
            best = max(best, cur)
        return best
