class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Time : O(n)
        maxBoi = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                maxBoi = max(maxBoi, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        return maxBoi
                
                
        
            
                