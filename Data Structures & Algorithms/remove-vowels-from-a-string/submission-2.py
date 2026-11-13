class Solution:
    def removeVowels(self, s: str) -> str:
        ans = []
        vowels = set(["a", "e" , "i", "o", "u"])
        for ch in s:
            if ch not in vowels:
                ans.append(ch)
            
        return "".join(ans)