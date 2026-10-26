class Solution:
    def isValid(self, s: str) -> bool:
        
        mp = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for p in s:
            if p not in mp:
                stack.append(p)
            else:
                if not stack:
                    return False
                if mp[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True