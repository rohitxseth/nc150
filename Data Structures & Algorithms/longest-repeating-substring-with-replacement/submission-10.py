class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        counter = {} 
        max_len = 0

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            count_max = max(counter.values())
            while (r - l + 1) - count_max > k:
                counter[s[l]] -= 1
                l += 1
            max_len = max(r - l + 1, max_len)
        
        return max_len