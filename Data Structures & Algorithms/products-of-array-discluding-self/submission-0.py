class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            product = 1

            for index, val in enumerate(nums):
                if(index != i):
                    product *= val
            
            result.append(product)

        return result