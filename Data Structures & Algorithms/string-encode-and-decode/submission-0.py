class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "🐵".join(strs)
        return encoded[::-1]

    def decode(self, s: str) -> List[str]:
        encoded = s[::-1]
        decoded = encoded.split("🐵")
        return decoded