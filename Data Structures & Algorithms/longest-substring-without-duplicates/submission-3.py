class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq_set = set()
        i = 0
        ans = 0

        for j in range(len(s)):
            while s[j] in freq_set:
                freq_set.remove(s[i])
                i = i + 1
            freq_set.add(s[j])
            ans = max(ans, j - i + 1)
        return ans





        