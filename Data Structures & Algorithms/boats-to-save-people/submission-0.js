class Solution {
    /**
     * @param {number[]} people
     * @param {number} limit
     * @return {number}
     */
    numRescueBoats(people, limit) {
        let sortedpep = people.sort((a,b)=>a-b)
        let result = 0
        let l = 0
        let r = people.length - 1

        while(l <= r){
            let curWeight = 0
            curWeight = curWeight + sortedpep[r]
            if(curWeight + sortedpep[l] <= limit){
                l++
            }
            result++
            r--
        }
        return result
    }
}
