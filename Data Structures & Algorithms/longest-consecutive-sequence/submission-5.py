class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maior = 0
        for num in numSet:
            consecutivo = num + 1
            if num - 1 not in numSet:
                tamSequencia = 1
                while consecutivo in numSet:
                    tamSequencia += 1
                    consecutivo += 1
                maior = max(maior, tamSequencia)
        return maior
            