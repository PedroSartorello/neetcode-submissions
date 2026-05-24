class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Basicamente tenho que descobrir qual numero inicia a sequencia
        # de numeros consecutivos.
        # Podemos usar um set para acessar O(1) e verificar se é inicio da sequencia
        numSet = set(nums)
        maior = [0]
        for num in nums:
            consecutivo = num + 1
            if num - 1 not in numSet:
                tamSequencia = 1
                while consecutivo in numSet:
                    tamSequencia += 1
                    consecutivo += 1
                maior.append(tamSequencia)
        return max(maior)
            