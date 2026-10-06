class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base_str = min(strs, key=len)
        ans = ""

        for i, char in enumerate(base_str):
            for s in strs:
                if s[i] != char:
                    return s[:i]

            
        
        return base_str



    
            




        