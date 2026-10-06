class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_s = [0]*26
        arr_t = [0]*26

        for char in s:
            arr_s[ord(char) - ord('a')] += 1
        for char in t:
            arr_t[ord(char) - ord('a')] += 1

        return arr_s == arr_t
           
        

        
        