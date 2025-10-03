class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bootlesDrunk = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            emptyBottles -= numExchange - 1
            numExchange += 1
            bootlesDrunk += 1
        
        return bootlesDrunk
        
