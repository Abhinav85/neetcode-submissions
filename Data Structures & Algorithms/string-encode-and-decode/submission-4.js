class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if(strs.length === 0) return null;
        const encodedStr = strs.join(":;")
        console.log("Encoded Str", encodedStr)
        return encodedStr
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        console.log("str", str)
        if(str === null) return []
        if (str === "") return [""]
        return str.split(":;")
    }
}
