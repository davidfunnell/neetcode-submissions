class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0

        while r < len(prices):
            valuation = prices[r]-prices[l]
            profit = max(profit, valuation)
            if prices[r] <= prices[l]:
                l = r
            r += 1
        return profit