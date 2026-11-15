class Solution:
    def isValid(self, s: str) -> bool:

        pairs = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            else:
                if stack and stack.pop() != pairs[ch]:
                    return False
                else:
                    return False
                
        
        return False if stack else True

