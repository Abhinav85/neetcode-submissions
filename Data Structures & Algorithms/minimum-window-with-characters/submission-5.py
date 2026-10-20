class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        map_t = {}
        for char in t:
            map_t[char] = map_t.get(char, 0) + 1

        need = len(map_t)
        have = 0

        map_s = {}
        i = 0

        res = float("inf")
        res_start = 0

        for j in range(len(s)):
            c = s[j]
            map_s[c] = map_s.get(c, 0) + 1

            if c in map_t and map_s[c] == map_t[c]:
                have += 1

            while have == need:
                if j - i + 1 < res:
                    res = j - i + 1
                    res_start = i

                map_s[s[i]] -= 1

                if s[i] in map_t and map_s[s[i]] < map_t[s[i]]:
                    have -= 1

                i += 1

        if res == float("inf"):
            return ""

        return s[res_start:res_start + res]