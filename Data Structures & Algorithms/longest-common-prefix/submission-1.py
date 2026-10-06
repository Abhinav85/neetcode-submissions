class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base_str = ""
        ans = ""
        min_length = float('inf')
        for s in strs:
            if len(s) < min_length:
                base_str = s
                min_length = len(s)

        for i, char in enumerate(base_str):
            for s in strs:
                if s[i] != char:
                    return ans

            ans = ans + char
        
        return ans



    
            




        