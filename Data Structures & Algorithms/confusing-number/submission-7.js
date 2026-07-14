class Solution {
    /**
     * @param {number} n
     * @return {boolean}
     */
    confusingNumber(n) {
        let comparison = []

        let value = String(n)

        for(let char of value){
            if(["2","3","4","5","7"].includes(char)){
                return false
            }
            if(char == "6"){
                comparison.push("9")
            }else if(char == "9"){
                comparison.push("6")
            }else{
                comparison.push(char)
            }
        }
        let answer = comparison.reverse().join("")
        console.log(comparison.reverse().join(""), value, n, String(n))
        if(value === answer){
            console.log(answer, value)
            return false
        }
        console.log("hi?")
        return true

    }
}
