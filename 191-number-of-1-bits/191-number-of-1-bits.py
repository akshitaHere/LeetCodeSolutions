class Solution:
    def hammingWeight(self, n: int) -> int:
        # Solution 1:
        res = 0
        while n:
            n = n & (n-1)
            res +=1
        return res
        
        
#        Solution 2: Time, Memory : O(n)
#        res = 0
#        while n:
#            res += n % 2
#            n = n >> 1
#        return res
    
        