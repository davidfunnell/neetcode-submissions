class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {

        let perm = new Map()
        let len = s1.length
        let compare = new Map()

        for(let char of s1){
            perm.set(char, 1 + (perm.get(char)||0))
        }
        for(let i = 0; i < s2.length; i++){
            if(i < (len - 1)){
                compare.set(s2[i], 1 + (compare.get(s2[i])||0))
            }else{
                let ans = true
                compare.set(s2[i], 1 + (compare.get(s2[i])||0))

                for(const [key, value] of perm){
                    if(compare.get(key) != value){
                        ans = false
                    }
                }
                if(ans == true){
                    return true
                }
                compare.set(s2[i-len+1], compare.get(s2[i-len+1]) - 1)
            }

        }
        return false

    }
}
