class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}
        for word in strs:
            freq_list = [0]*26
            for char in word:
                freq_list[ord(char) - ord('a')] += 1
            
            freq_tuple = tuple(freq_list)
            
            if freq_tuple in freq_map:
                freq_map[freq_tuple].append(word)
            else:
                freq_map[freq_tuple] = [word]

        return list(freq_map.values())
        
        