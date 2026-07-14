class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights)-1

        while l < r:
            distance = r - l
            height = min(heights[l], heights[r])
            area = max(area, (height*distance))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return area