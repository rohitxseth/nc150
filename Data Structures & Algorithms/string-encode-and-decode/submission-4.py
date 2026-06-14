class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        encoded = "🐵".join(strs)
        return encoded[::-1]

    def decode(self, s: str) -> List[str]:
        if s == []:
            return [""]
        encoded = s[::-1]
        decoded = encoded.split("🐵")
        return list(decoded)