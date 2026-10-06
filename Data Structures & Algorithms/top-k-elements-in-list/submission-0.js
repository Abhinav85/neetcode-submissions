class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(arr, k) {
        let countObj = {};
	    let countArr = Array.from({length: arr.length+ 1}, () => []);
	    for (const num of arr) {
            if(countObj[num]){
                countObj[num] = countObj[num] + 1
            }else{
                countObj[num] = 1
            }
        }


        for (const n in countObj) {
            countArr[countObj[n]].push(parseInt(n))
        }

        const res = []

        for(let i = countArr.length - 1; i > 0 ; i--){
            for (const n of countArr[i]){
                res.push(n)
                if(res.length === k) return res
            }
        }

    }
}
