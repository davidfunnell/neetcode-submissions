class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        valdict = {}
        
        for l in range(len(nums)-1):
            val2 = nums[l]

            for r in range(l+1, len(nums)):
                val3 = nums[r]

                curTotal = val2 + val3
                need = 0 - curTotal

                if need in valdict:
                    for index in valdict[need]:
                        tempList = sorted([need, val2, val3])
                        if tempList not in result:
                            result.append(tempList)

            if val2 in valdict:
                valdict[val2].append(l)
            else:
                valdict[val2] = [l]



        return result