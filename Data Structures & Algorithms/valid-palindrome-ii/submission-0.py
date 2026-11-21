class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkvalid(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l,r=l+1,r-1
            return True
        l,r=0,len(s)-1

        while l<r:
            if s[l]!=s[r]:
                return(checkvalid(l+1,r) or checkvalid(l,r-1))
            l,r=l+1,r-1
        return True