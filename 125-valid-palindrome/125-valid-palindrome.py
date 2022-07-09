class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        a = ''.join(filter(str.isalnum,lower))
        print(a)
        rev = a[::-1]
        print(rev)
        return a == rev
            
         
     
        
        
        
        
       