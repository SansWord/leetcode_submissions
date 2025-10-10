class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.length = len(prices)
        self.mem = [(-1,"NOOP")] * self.length
        result = self.findProfit(prices, 0)
        return result
    
    def findProfit(self, prices, nThDay: int) -> int:
        if nThDay >= self.length:
            return 0

        if self.mem[nThDay][0] != -1:
            return self.mem[nThDay][0]

        buyTodayProfit = 0
        sellAtNthDay = None
        pToday = prices[nThDay]
        for i in range(nThDay+1, self.length):
            iPrice = prices[i]
            if iPrice > pToday:
                profit = iPrice - pToday + self.findProfit(prices, i + 2)
                if profit > buyTodayProfit:
                    buyTodayProfit = profit
                    sellAtNthDay = i

        skipTodayProfit = self.findProfit(prices, nThDay + 1)

        if skipTodayProfit >= buyTodayProfit:
            result = skipTodayProfit
            action = "skip"
        else:
            result = buyTodayProfit
            action = f"buy, sell at {sellAtNthDay}th day"
        
        self.mem[nThDay] = (result, action)
        return result
