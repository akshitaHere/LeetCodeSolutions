class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Solution 1
        return sorted(s) == sorted(t)
        
        
        