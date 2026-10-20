class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        i = 0
        j = 1
        freq_map[s[i]] = 1
        max_freq = 1
        ans = 0
        if len(s) == 1:
            return 1

        while i < j and j < len(s):
            freq_map[s[j]] = freq_map.get(s[j],0) + 1
            max_freq = max(freq_map[s[j]], max_freq)
            while j - i + 1 - max_freq > k:
                freq_map[s[i]] = freq_map[s[i]] - 1
                i = i + 1
            ans = max(ans, j - i + 1)
            j = j +1

        return ans
        