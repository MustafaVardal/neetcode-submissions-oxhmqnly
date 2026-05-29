class Solution:

    def encode(self, strs: List[str]) -> str:
        word_encode = ""
        for word in strs:
            word_encode += str(len(word)) + "$" + word
        return word_encode
    def decode(self, s: str) -> List[str]:
        list_word = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            size = int(s[i:j])
            print(size)
            i = j + 1
            j = i + size
            list_word.append(s[i:j])
            i = j
        return list_word