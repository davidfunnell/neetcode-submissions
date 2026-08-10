class Solution {
    /**
     * @param {number[][]} mat
     * @return {number}
     */
    smallestCommonElement(mat) {
        let length_mat = mat.length
        
        const mat_map = new Map()

        for(let i = 0; i < length_mat; i++){
            for(let value of mat[i]){
                mat_map.set(value,(mat_map.get(value) | 0) + 1)
            }
        }

        for(let cur_val of mat[0]){
            if(mat_map.get(cur_val) == length_mat){
                return cur_val
            }
        }
        return -1
    }
}
