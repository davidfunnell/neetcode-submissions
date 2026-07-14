class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        compare = set(nums)

        return len(compare) != len(nums)