class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs is [""]: 
            return ""

        encoded_str = ""
        for s in strs:
            l = str(len(s))
            encoded_str += l + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s is "":
            return [""]
        decoded = []
        i = 0
        while i < len(s):
            l = int(s[i])
            decoded.append(s[i + 2 : i + 2 + l])
            i += 2 + l
        return decoded
            





