class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visto = {}
        for i, num in enumerate(nums):
            dif = target - num
            if dif in visto:
                return [visto[dif], i]
            visto[num] = i