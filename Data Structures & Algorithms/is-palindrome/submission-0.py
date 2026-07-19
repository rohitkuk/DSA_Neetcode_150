class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([el.lower() for el in s if el.isalnum()])
        l, r = 0, len(s)-1
        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
