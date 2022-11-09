class Solution:
    def fib(self, n: int) -> int:
        fibonacci_cache = {}
        
        def fibonacci_memo(n):
            if n in fibonacci_cache:
                return fibonacci_cache[n]
            elif n <= 1:
                fibonacci_cache[n] = n
                return n
            else:           
                fibonacci_cache[n] =  fibonacci_memo(n -1) + fibonacci_memo(n -2)
                return fibonacci_cache[n]
        
        return fibonacci_memo(n)