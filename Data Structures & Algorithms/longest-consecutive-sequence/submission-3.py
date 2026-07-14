class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numsDict = {}

        for index, val in enumerate(nums):
            numsDict[val] = index
        
        minVal = min(nums)
        maxVal = max(nums)
        longest = 0
        length = 0


        for i in range(minVal, maxVal+1):
            
            if i in numsDict:
                length += 1
            else:
                length = 0

            longest = max(length, longest)

        return longest