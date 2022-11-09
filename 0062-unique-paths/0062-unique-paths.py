class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Solution 1: Memoized recursive dp
        #Time : O(m*n), Space : O(m*n)
        #@cache
        cache = {}
        def pathFinder(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            elif i >= m or j >= n:
                return 0
            elif i == m - 1 and j == n - 1:
                return 1
            cache[(i, j)] = pathFinder(i, j + 1) + pathFinder(i + 1, j)
            return cache[(i, j)]
        return pathFinder(0, 0)
        
        