class Solution {
    /**
     * @param {number} numRows
     * @return {number[][]}
     */
    generate(numRows) {
        let result = []

        for(let row = 1; row <= numRows; row++){
            let tempArr = []

            for(let col = 1; col <= row; col++){
                if(col == 1 || col == row){
                    tempArr.push(1)
                }else{
                    let tempVal = result[row-2][col-1] + result[row-2][col-2]
                    tempArr.push(tempVal)
                }

            }
            result.push(tempArr)
        }

        return result
    }
}
