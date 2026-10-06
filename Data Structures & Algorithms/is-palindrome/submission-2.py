class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(c for c in s if c.isalnum())
        r = 0
        l = len(s) - 1



        while (r <= l):
            if s[r].lower() != s[l].lower():
                return False
            r = r + 1
            l = l - 1
        return True
        