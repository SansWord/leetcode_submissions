class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # find min two sum of list, using two points
        l = 0
        r = len(prices)-1

        minSum = float("inf")
        while l < r:
            lP = prices[l]
            rP = prices[r]
            currSum = lP + rP
            minSum = min(minSum, currSum)

            if lP < rP:
                r -= 1
            else:
                l += 1
        
        return money if money < minSum else money - minSum
        
