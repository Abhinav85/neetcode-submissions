class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(string1, string2) {
        if(string1.length !== string2.length) return false;
	    const obj1 = {};
	    const obj2 = {};
	    for (let c of string1){
		    if(obj1[c]) {
			    obj1[c] = obj1[c] + 1
            }else{
	            obj1[c] = 1
            }           
        }

        for (let c of string2){
            if(obj2[c]) {
                obj2[c] = obj2[c] + 1
            }else{
                obj2[c] = 1
            }
        }

        if(Object.keys(obj1).length !== Object.keys(obj2).length) return false;

        for(let key of Object.keys(obj1)){
            if(obj2[key] !== obj1[key]){
                return false
            }
        }
        return true

    }
}
