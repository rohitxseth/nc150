class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charMap = {}
        left = 0
        best = 0

        for right, char in enumerate(s):
            if char in charMap:
                left = max(charMap[char] + 1, left)
            best = max(best, right - left + 1)
            charMap[char] = right

        return best    