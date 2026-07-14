class Solution {
    /**
     * @param {string[]} logs
     * @return {number}
     */
    minOperations(logs) {
        let logStack = []

        for(let log of logs){
            if(log == "../"){
                logStack.pop()
            }else if(log != "./"){
                logStack.push(log)
            }
        }
        return logStack.length
    }
}
