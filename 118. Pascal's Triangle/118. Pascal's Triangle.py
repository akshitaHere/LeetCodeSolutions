class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #Dynamic programming
        #Time : O(n^2), Space : O(n^2)
        res = []
        res.append([1])
        if numRows == 1: return res
        res.append([1, 1])
        if numRows == 2: return res

        for i in range(2, numRows):
            level = [1]
            for j in range(1, len(res[i - 1])):
                level.append(res[i - 1][j - 1] + res[i - 1][j])
            level.append(1)
            res.append(level)
        return res
        
    #                        OR
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        dp = res[-1]
        for i in range(2, numRows):
            nextDP = [1] * (len(dp) + 1)
            for j in range(1, len(nextDP) - 1):
                nextDP[j] = dp[j - 1] + dp[j]
            dp = nextDP
            res.append(dp)
        return res