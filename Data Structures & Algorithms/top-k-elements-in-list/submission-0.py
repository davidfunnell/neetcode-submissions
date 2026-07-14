class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numDict = {}
        sortedDict = []
        result = []

        for num in nums:
            numDict[num] = 1 + numDict.get(num, 0)

        for key in numDict:
            sortedDict.append([numDict[key], key])
        
        sortedDict.sort(reverse = True)

        for i in range(k):
            result.append(sortedDict[i][1])
   

        return result

        