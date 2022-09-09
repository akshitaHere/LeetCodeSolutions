class Solution:
    def hammingWeight(self, n: int) -> int:
        #Time : O(1)
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res
        
#        Solution 2: Time : O(32) (no of bits) = O(1)
#        res = 0
#        while n:
#            res += n % 2
#            n = n >> 1
#        return res
    
        
        