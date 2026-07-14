class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums) {
        let counter = 0

        let temp = 0

        for(let val of nums){
            if(val == 1){
                temp++
                counter = Math.max(counter, temp)
            }else{
                temp = 0
            }
        }
        return counter
    }
}
