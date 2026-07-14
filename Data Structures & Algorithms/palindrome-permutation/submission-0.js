class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    canPermutePalindrome(s) {
        const map = new Map();
        let mid = 0

        for(let char of s){
            map.set(char, (map.get(char) || 0) + 1)
        }

        for(const [key, value] of map){
            if(value%2>0){
                mid++
            }
            if(mid > 1){
                return false
            }

        }
        return true
    }
}
