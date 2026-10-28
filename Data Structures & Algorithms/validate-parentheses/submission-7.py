class Solution:
    def isValid(self, s: str) -> bool:
        
        open_close = { "(" : ")" , "{" : "}", "[" : "]" }
        stack = []

        for ch in s:
            if ch in open_close:
                if stack and not open_close[ch] == stack[-1]:
                    return False
            else:
                stack.append(ch)
        return True