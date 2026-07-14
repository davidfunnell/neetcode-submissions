class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        valDict = {}

        for i, val in enumerate(nums):
            valDict[val] = i
        
        for j, val in enumerate(nums):
            diff = target - val
            if diff in valDict and valDict[diff] != j:
                return [min(valDict[diff],j), max(valDict[diff], j)]