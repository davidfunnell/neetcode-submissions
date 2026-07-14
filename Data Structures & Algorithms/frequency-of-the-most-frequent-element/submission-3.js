class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    maxFrequency(nums, k) {
        let result = 0
        nums.sort((a,b) => a - b)
        if(nums.length == 1){
            return 1
        }

        for(let r = nums.length - 1; r >= 1; r--){
            let l = r - 1
            let count = k
            let match = nums[r]
            let tempResult = 1
            while(count > 0 && l >= 0){
                count = count - (match - nums[l])
                if(count >= 0){
                    tempResult++
                    l--
                }
            }
            result = Math.max(result, tempResult)
        }
        return result

    }
}
