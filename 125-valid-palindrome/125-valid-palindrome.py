class Solution:
    def isPalindrome(self, s: str) -> bool:
          #Solution 3
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.isIsalnum(s[l]):
                l += 1
            while r > l and not self.isIsalnum(s[r]):
                r -= 1    
            if not s[l].lower() == s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
    def isIsalnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
