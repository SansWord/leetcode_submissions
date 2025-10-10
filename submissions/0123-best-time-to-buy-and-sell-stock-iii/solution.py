class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        compressedPrices = []

        findMin = True
        preVal = prices[0]
        for i in range(1, len(prices)):
            val = prices[i]
            if findMin:
                if val > preVal:
                    compressedPrices.append(preVal)
                    findMin = not findMin
            else:
                if val < preVal:
                    compressedPrices.append(preVal)
                    findMin = not findMin
            preVal = val
        
        compressedPrices.append(preVal)

        # remove all intemidiate points and only keep local minimum and maximum
        prices = compressedPrices
    

        LENGTH = len(prices)
        if LENGTH <= 1:
            return 0

        leftMaxProfit = [0] * LENGTH

        lMin = prices[0]
        for i in range(1, LENGTH):
            p = prices[i]
            if p < lMin:
                lMin = p
                leftMaxProfit[i] = leftMaxProfit[i-1]
            else:
                leftMaxProfit[i] = max(leftMaxProfit[i-1], p - lMin)

        rightMaxProfit = [0] * LENGTH

        rMax = prices[-1]
        for i in range(LENGTH-2, -1, -1):
            p = prices[i]
            if p > rMax:
                rMax = p
                rightMaxProfit[i] = rightMaxProfit[i+1]
            else:
                rightMaxProfit[i] = max(rightMaxProfit[i+1], rMax - p)

        maxProfit = 0
        for i in range(LENGTH):
            maxProfit = max(maxProfit, leftMaxProfit[i] + rightMaxProfit[i])
        
        return maxProfit
        
    
    
        
