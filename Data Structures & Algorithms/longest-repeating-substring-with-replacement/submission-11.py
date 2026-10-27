class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = defaultdict(int)
        l = 0
        max_len = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            most_frequent = max(counter.values())
            while (r - l + 1) - most_frequent > k:
                counter[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len