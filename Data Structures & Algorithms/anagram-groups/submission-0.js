class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(arr) {
        const positionObj = {};
	    for (const word of arr) {
		const sortedWord = [...word].sort().join("");
        console.log(sortedWord)
            if(positionObj[sortedWord]){
                positionObj[sortedWord].push(word)
            }
            else{
                positionObj[sortedWord] = [word]
            }
        }
        return Object.values(positionObj)
    }
}
