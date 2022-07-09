class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        a = ''.join(filter(str.isalnum,lower))
        print(a)
        return a == a[::-1]
            
         
     
        
        
        
        
       