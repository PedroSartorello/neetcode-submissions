class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contador = {}
        for num in nums:
            if num in contador:
                return True
            else: 
                contador[num] = 1
        return False
        
        