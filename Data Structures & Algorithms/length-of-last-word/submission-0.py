class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        word = s.split().pop()
        return len(word)