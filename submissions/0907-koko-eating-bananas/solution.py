class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # search for k?
        # to calculate t, requires time for a k, sum ceil(piles[i] / k)
        # if t is smaller than h, increase else decrease
        # problem: calculation t might takes too long, any way to improve it?

        maxPileCount = 0
        for bananas in piles:
            maxPileCount = max(maxPileCount, bananas)
        
        lower = 0
        upper = maxPileCount

        while upper - lower > 1:
            mid = lower + (upper-lower)//2

            time = 0
            for bananas in piles:
                time += ceil(bananas/mid)
            
            if time > h:
                # too slow
                lower = mid
            else:
                upper = mid
        
        return upper

        
