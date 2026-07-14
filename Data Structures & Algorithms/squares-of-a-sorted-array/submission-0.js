class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    sortedSquares(nums) {

        let temp = []
        for(let num of nums){
            temp.push(num*num)
        }
        return temp.sort((a,b) => a - b)
    }
}
