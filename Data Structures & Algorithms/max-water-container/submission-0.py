class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        maxArea = 0

        while left < right:
            altura = min(heights[right], heights[left])
            area = (right-left) * altura
            maxArea = max(maxArea, area)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        
        return maxArea
        




        return maxArea


