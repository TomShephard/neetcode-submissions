class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not self.isalnum1(s[l]):
                l += 1
            while l < r and not self.isalnum1(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        
        return True
    
    def isalnum1(self, x):
        return (ord('a') <= ord(x) <= ord('z') or ord('A') <= ord(x) <= ord('Z') or ord('0') <= ord(x) <= ord('9'))
            
        