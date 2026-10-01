class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) +  "#" + s
        return res

    #- 5#hello5#world

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i : j])
            ans.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return ans