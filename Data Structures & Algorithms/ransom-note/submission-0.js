class Solution {
    /**
     * @param {string} ransomNote
     * @param {string} magazine
     * @return {boolean}
     */
    canConstruct(ransomNote, magazine) {
        let magDict = new Map()

        for(let char of magazine){
            magDict.set(char, 1 + (magDict.get(char) || 0))
        }

        for(let char of ransomNote){
            if(magDict.has(char) && magDict.get(char) > 0){
                magDict.set(char, magDict.get(char) - 1)
            }else{
                return false
            }
        }
        return true
    }
}
