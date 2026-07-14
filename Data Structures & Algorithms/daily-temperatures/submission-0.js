class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let result = []

        for(let i = 0; i < temperatures.length; i++){
            let pointer = i
            let found = false
            while(found == false && pointer < temperatures.length){
                if(temperatures[i] >= temperatures[pointer]){

                    pointer++
                }else{
                    found = true
                }
            }

            if(found == true){
                result.push(pointer - i)
            }else{
                result.push(0)
            }

        }
        return result
    }
}
