class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        result = -1
        numsDict = {}

        for num in nums:
            numsDict[num] = 1 + numsDict.get(num, 0)

        for key, value in numsDict.items():
            if value == 1 and key > result:
                result = key

        return result