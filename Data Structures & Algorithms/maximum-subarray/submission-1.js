class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        let max = nums[0];
        let cur = 0;

        for (let n in nums) {
            cur = cur > 0 ? cur : 0;
            cur += nums[n];
            max = max > cur ? max : cur;
        }

        return max;
    }
}
