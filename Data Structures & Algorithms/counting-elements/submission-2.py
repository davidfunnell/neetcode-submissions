class Solution:
    def countElements(self, arr: List[int]) -> int:
        arrDict = {}

        for key in arr:
            arrDict[key] = 1 + arrDict.get(key, 0)


        result = 0

        for item in arr:
            if (item + 1) in arrDict:
                result += 1

        
        return result