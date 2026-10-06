class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(arr, sum) {
        for( let i = 0; i < arr.length-1;i++){
		    let num = arr[i];
		    let sumToFind = sum - num;
		    for (let j = i+1; j < arr.length; j++) {
			    if(arr[j] === sumToFind) return [i,j]
            }
        }

    }
}
