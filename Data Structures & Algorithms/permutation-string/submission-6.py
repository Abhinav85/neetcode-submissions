class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq_map_s1 = {}
        for char in s1:
            freq_map_s1[char] = freq_map_s1.get(char,0) + 1

        # Now open a window of len(s1) size on s2
        i = 0
        n = len(s1)
        freq_map_s2 = {}
        while i < n:
            freq_map_s2[s2[i]] = freq_map_s2.get(s2[i],0) + 1
            i = i + 1

        if freq_map_s2 == freq_map_s1:
            return True

        while i < len(s2):
            freq_map_s2[s2[i-n]] = freq_map_s2[s2[i-n]] - 1
            if freq_map_s2[s2[i-n]] == 0:
                del freq_map_s2[s2[i-n]]
            freq_map_s2[s2[i]] = freq_map_s2.get(s2[i],0) + 1
            if freq_map_s2 == freq_map_s1:
                return True
            i = i + 1
        
        return False


        