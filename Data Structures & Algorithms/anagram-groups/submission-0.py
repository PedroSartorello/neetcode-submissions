class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupo = {} # Anagrama sorted : [Lista]
        for palavra in strs:
            chave = str(sorted(palavra))
            if chave not in grupo:
                grupo[chave] = []
            grupo[chave].append(palavra)
        return list(grupo.values())