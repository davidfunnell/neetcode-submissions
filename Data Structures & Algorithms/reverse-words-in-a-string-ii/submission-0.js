class Solution {
    /**
     * @param {character[]} s
     * @return {void} Do not return anything, modify s in-place instead.
     */
    reverseWords(s) {

        let l = 0
        let r = s.length - 1

        while(l < r){
            let temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l++
            r--
        }
        
        let pointer = 0

        for(let i = 0; i <= s.length;i++){
            if(s[i] == " " || i == s.length){
                r = i-1
                l = pointer
                while(l < r){
                    let temp = s[l]
                    s[l] = s[r]
                    s[r] = temp
                    l++
                    r--
                }
                pointer = i + 1
            }
        }



    }
}
