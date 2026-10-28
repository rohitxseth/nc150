class Solution:
    def isValid(self, s: str) -> bool:
        
        close_open = {")" : "(" , "}" : "{", "]" : "["}
        stack = []
        valid = False

        for ch in s:
            if ch in close_open:
                if not stack:
                    return False
                if close_open[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        if stack:
            return False
        return True