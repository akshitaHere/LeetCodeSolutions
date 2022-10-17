class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for num in range(2, n):
            if primes[num]:
                for multiple in range(num**2, n, num):
                    primes[multiple] = False
                
        return sum(primes)