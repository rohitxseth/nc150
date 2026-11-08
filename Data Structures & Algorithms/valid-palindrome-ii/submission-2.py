class Solution:
    def validPalindrome(self, s: str) -> bool:
        l ,r = 0, len(s) - 1
        k = 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                if k > 0:
                    if s[l] == s[r - 1]:
                        r -= 1
                        k -= 1
                    elif s[l + 1] == s[r]:
                        l += 1
                        k -= 1
                else:
                    return False
            l += 1
            r -= 1
        
        return True