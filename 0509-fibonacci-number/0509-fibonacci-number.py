class Solution:
    def fib(self, n: int) -> int:
#        Solution 1 : Dp recursive : Time : 2^n, Space : O(n)
#       if n <= 1:
#           return n
#       return self.fib(n - 1) + self.fib(n - 2)

#        Solution 2 : Dp recursive with memoization : Time : O(n), Soace : O(n)
        cache = {}
        def fibCalc(n):
            if n in cache:
                return cache[n]
            elif n <= 1:
                cache[n] = n
                return n
            else:           
                cache[n] =  fibCalc(n -1) + fibCalc(n -2)
                return cache[n]
        return fibCalc(n)
    
#        Solution 3 : Iterative
#        Time : O(n), Space : 1
        if n <= 1:
            return n
        
        f0, f1 = 0, 1
        for i in range(2, n + 1):
            fi = f0 + f1
            f0 = f1
            f1 = fi
        return f1