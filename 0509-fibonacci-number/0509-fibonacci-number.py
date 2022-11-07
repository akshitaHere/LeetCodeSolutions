class Solution:
    def fib(self, n: int) -> int:
        #Solution 1
        #Time : O(n), Space : 1
        if n <= 1:
            return n
        
        f0, f1 = 0, 1
        if n == 0: return 0
        if n == 1: return 1
        fi = 0
        for i in range(2, n + 1):
            fi = f0 + f1
            f0 = f1
            f1 = fi
        
        return f1
    
        #Solution 2
        #Time : O(n), Space : O(n)
        #f = []
        #f.append(0)
        #f.append(1)
        
        #for i in range(2, n+1):
        #    f.append(f[i-1] + f[i-2])
        
        #return f[n]
    