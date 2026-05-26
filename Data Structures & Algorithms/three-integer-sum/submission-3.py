class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:                
                if nums[left] + nums[right] == -num:
                    res.append([num, nums[left], nums[right]]) 
                    left+=1
                    right -=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    if nums[left] + nums[right] < -num:
                        left+=1
                    else:
                        right -=1

        return res 
