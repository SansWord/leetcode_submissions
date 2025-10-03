class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        bottleLeft = numBottles
        sum = bottleLeft
        while bottleLeft >= numExchange:
            sum += bottleLeft // numExchange
            bottleLeft = bottleLeft % numExchange + bottleLeft // numExchange

        return sum
        
