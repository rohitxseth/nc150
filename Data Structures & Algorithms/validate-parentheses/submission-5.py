class Solution:
    def isValid(self, s: str) -> bool:
        
        open_close = { "(" : ")" , "{" : "}", "[" : "]" }
        stack = []

        for ch in s:
            if ch not in open_close:
                stack.append(ch)
            else:
                if stack and not open_close[ch] == stack[-1]:
                    return False
        return True