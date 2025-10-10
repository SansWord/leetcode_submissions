class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find maximum gap of prices
        # two pointer?

        l = 0
        r = 1
        maxProfit = 0
        length = len(prices)

        while l < r and r < length:
            lVal = prices[l]
            rVal = prices[r]
            profit = rVal - lVal
            if profit < 0:
                l = r
            else:
                maxProfit = max(maxProfit, profit)
            r = r + 1
        
        return maxProfit


            # decide where to move

        
