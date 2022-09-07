class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxBoi = 0
        l = 0
        r = l + 1
        while r < len(prices):
            if prices[l] < prices[r]:
                maxBoi = max(maxBoi, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        return maxBoi
                