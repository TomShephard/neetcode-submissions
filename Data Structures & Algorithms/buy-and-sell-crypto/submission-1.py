class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        maxprofit = 0

        while r < len(prices):

            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxprofit = max(profit, maxprofit)
                r += 1
            else:
                l = r
                r = l + 1
        return maxprofit
