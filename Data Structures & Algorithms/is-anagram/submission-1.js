class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let sMap = new Map()
        let tMap = new Map()

        for(let char of s){
            sMap.set(char, 1 + (sMap.get(char) || 0))
        }
        for(let char of t){
            tMap.set(char, 1 + (tMap.get(char) || 0))
        }

        for(const [key, value] of sMap){
            if(tMap.get(key) != value){
                return false
            }
        }
        for(const [key, value] of tMap){
            if(sMap.get(key) != value){
                return false
            }
        }

        return true
    }
}
