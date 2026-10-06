class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(arr, sum) {
        let map = new Map();
	        for ( let index in arr) {
                console.log(map)
                console.log(index)
		        const sumToFind = sum - arr[index];
                console.log(sumToFind)
		        if ( map.has(sumToFind)){
			        let firstIndex = map.get(sumToFind);
			        return [ parseInt(firstIndex), parseInt(index)]
                }
                map.set(arr[index], index);
        }

        return [-1, -1]

    }
}
