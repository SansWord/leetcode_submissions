class Solution:
    def arrangeCoins(self, n: int) -> int:
        return floor(((n * 8 + 1)**(1/2) - 1)/2)
        
