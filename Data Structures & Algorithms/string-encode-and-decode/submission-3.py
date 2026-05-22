class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            lenght = int(s[i:j])
            start = j + 1
            end = lenght + start
            word = s[start:end]
            res.append(word)
            i = end
        return res