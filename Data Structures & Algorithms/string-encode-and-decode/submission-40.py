class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        if not strs:
            return ""
        for word in strs:
            encoded += str(len(word)) + "$" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            size = int(s[i : j])
            i = j + 1
            j = i + size
            decoded.append(s[i:j])
            i = j
        return decoded