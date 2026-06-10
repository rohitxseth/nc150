class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded: str = ""
        for s in strs:
            l: int = len(s)
            encoded = encoded + str(l) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        i: int = 0
        res: List = []

        while i < len(s):
            j: int = i
            while s[j] != "#":
                j += 1
            l: int = int(s[i:j])
            res.append(s[j+1 : j+1+l])
            i = j + 1 + l
        return res

