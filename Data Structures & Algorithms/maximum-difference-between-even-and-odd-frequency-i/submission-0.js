class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    maxDifference(s) {
        let sCount = new Map()

        for(let char of s){
            sCount.set(char, 1 + (sCount.get(char) || 0))
        }

        let maxOdd = 0
        let minEven = Infinity

        for(let [key, value] of sCount){
            if(value % 2 > 0){
                maxOdd = Math.max(maxOdd, value)
            }else{
                minEven = Math.min(minEven, value)
            }
        }
        return maxOdd-minEven
    }
}
