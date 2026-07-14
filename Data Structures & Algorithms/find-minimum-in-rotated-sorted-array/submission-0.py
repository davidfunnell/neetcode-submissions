class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            middle = math.floor((l + r) /2)
            print(middle)
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle 
        
        return nums[r]

