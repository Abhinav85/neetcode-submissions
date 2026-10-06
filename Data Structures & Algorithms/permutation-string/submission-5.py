class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)
        l = 0
        r = l
        baselineArr = [0]*26
        compareArr = [0]*26


        for char in s1:
            ascii = ord(char) - 97
            baselineArr[ascii] = baselineArr[ascii] + 1
        while r < len(s2):           
            ascii = ord(s2[r]) - 97
            compareArr[ascii] = compareArr[ascii] + 1

            if (r - l >= k):
                ascii = ord(s2[l]) - 97
                compareArr[ascii] = compareArr[ascii] - 1
                l = l + 1

            r = r + 1
            if compareArr == baselineArr and r - l == k:
                return True

        return False
