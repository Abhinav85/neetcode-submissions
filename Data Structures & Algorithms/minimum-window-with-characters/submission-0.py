class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        base_hash = {}
        for char in t:
            if char in base_hash:
                base_hash[char] += 1
            else:
                base_hash[char] = 1

        l = 0
        r = l
        sub_str = ""
        compare_set = {}
        print(base_hash)
        while r < len(s):
            if s[r] in compare_set:
                compare_set[s[r]] += 1
            else:
                compare_set[s[r]] = 1
            print (compare_set)


            while all(compare_set.get(char, 0) >= base_hash.get(char, 0) for char in base_hash):
                print("in the loop")
                sub_str_new = s[l:r + 1]
                print("sub_str", sub_str_new, r + 1, l)
                if len(sub_str_new) < len(sub_str) or sub_str == "":
                    sub_str = sub_str_new
                compare_set[s[l]] -= 1
                l += 1
            r += 1

        return sub_str