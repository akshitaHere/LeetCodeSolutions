class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def pathFinder(i, j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return pathFinder(i, j + 1) + pathFinder(i + 1, j)
        return pathFinder(0, 0)