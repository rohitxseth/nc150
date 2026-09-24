class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[i] != "#":
                i += 1
            if s[i] == "#":
                l = int(s[j:i])
                decoded_strs.append(s[i+1 : i+1+l])
                i += 1 + l
        return decoded_strs