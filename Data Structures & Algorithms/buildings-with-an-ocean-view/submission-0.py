class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        result = []

        curHeight = 0

        for i in range(len(heights)-1, -1,-1):
            if heights[i] > curHeight:
                curHeight = heights[i]
                result.append(i)
        
        return result[::-1]