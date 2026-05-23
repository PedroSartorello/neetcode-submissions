class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            produto = 1
            for j, num in enumerate(nums):
                if i!= j:
                    produto *= num
            res.append(produto)
        return res