class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            l = str(len(s))
            encoded_str += l + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[i] != "#":
                i += 1
            l = int(s[j:i])
            decoded.append(s[i + 1 : i + 1 + l])
            i = i + 1 + l
        return decoded

            





