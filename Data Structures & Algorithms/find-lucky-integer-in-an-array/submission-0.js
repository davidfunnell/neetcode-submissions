class Solution {
    /**
     * @param {number[]} arr
     * @return {number}
     */
    findLucky(arr) {
        let arrMap = new Map()

        for(let val of arr){
            arrMap.set(val, 1 + (arrMap.get(val)||0))
        }

        let result = -1

        for(let [key, value] of arrMap){
            if(key == value){
                result = Math.max(key, result)
            }
        }
        return result
    }
}
