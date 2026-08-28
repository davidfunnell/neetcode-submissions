class Solution {
    /**
     * @param {number[]} arr
     * @return {number[]}
     */
    replaceElements(arr) {

        let maxlength = arr.length

        for(let i = 0; i < maxlength - 1; i++){
            let maxval = Math.max(...arr.slice(i + 1,maxlength))
            arr.splice(i,1,maxval)

        }

        arr.splice(maxlength-1,1,-1)

        return arr

    }
}
