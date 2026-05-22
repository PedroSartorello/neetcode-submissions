class Solution:

    def encode(self, strs: List[str]) -> str:
        for i, element in enumerate(strs):
            strs[i] = str(len(element))+ '#' + element
        print(''.join(strs))
        return ''.join(strs)

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