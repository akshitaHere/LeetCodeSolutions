class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        
        #Solution 2 : DP recursive
        #Time : O(n), Space : O(n)
        f = []
        f.append(0)
        f.append(1)
    
        for i in range(2, n+1):
            f.append(f[i-1] + f[i-2])
        
        return f[n]
    