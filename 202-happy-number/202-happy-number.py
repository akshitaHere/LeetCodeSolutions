class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()
        
        while n not in hashSet:
            hashSet.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False
    
    def sumOfSquares(self, n: int) -> int:
        squareSum = 0
        while(n):
            squareSum += (n%10) * (n%10)
            n = n//10
        return squareSum
    
    