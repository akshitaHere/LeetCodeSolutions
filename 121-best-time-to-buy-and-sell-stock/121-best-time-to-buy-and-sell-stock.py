class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r, maxBoi = 0, 1, 0
        while r < len(prices):
            #profitable
            
            if prices[l] < prices[r]:
                maxBoi = max(maxBoi, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        return maxBoi
        