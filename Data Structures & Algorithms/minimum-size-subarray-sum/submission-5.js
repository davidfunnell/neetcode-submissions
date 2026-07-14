class Solution {
    /**
     * @param {number} target
     * @param {number[]} nums
     * @return {number}
     */
    minSubArrayLen(target, nums) {
        let l = 0
        let r = 0
        let targetSum = 0
        let result = Infinity

        while(r <= nums.length){
            targetSum += nums[r]
            while(targetSum >= target){
                result = Math.min(result, r - l + 1)
                targetSum -= nums[l]
                l++
            
            }
            r++
        }
        return result === Infinity ? 0 : result
    }
}
