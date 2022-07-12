class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxBoi = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                maxBoi = max(prices[r] - prices[l], maxBoi)
                r += 1
            else:
                l = r
                r = l + 1
        return maxBoi
        