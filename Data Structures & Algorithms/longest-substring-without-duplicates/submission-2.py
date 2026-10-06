class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        r = 1
        charSet = set()
        charSet.add(s[l])
        max_length = r-l

        while r < len(s):
            if s[r] in charSet:
                charSet.remove(s[l])
                l = l + 1
            else:
                charSet.add(s[r])
                r = r + 1
            max_length = max(max_length, r - l)




        return max_length

        