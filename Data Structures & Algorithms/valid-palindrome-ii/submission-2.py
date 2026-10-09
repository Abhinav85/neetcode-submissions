class Solution:
    def validPalindrome(self, s: str) -> bool:
        chance = True
        def isPalindrome(s,l,r): 
            nonlocal chance
            i = l
            j = r
            while i < j:
                if s[i] != s[j]:
                    if chance:
                        chance = False
                        return isPalindrome(s,i+1,j) or isPalindrome(s,i,j-1)
                    else:
                        return False

                else:
                    i = i +1
                    j = j  - 1
            return True

        return isPalindrome(s,0,len(s)-1)


        