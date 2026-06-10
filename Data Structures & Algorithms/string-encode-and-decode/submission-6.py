class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "EMPTY_LIST"
        encoded = "🐵".join(strs)
        return encoded[::-1]

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY_LIST":
            return []
        if s == "":
            return [""]
        encoded = s[::-1]
        decoded = encoded.split("🐵")
        return list(decoded)