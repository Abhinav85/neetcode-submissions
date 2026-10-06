class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)
        l = 0
        r = l + k
        while r <= len(s2):
            substring = s2[l:r]
            substring = ''.join(sorted(substring))
            s1 = ''.join(sorted(s1))
            print(s1, substring)
            if s1 == substring:
                return True
            else:
                l = l + 1
                r = l + k
            print(r,l);
        return False
