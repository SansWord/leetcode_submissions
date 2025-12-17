class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0
        for f in fruits:
            found = False
            for i in range(0, len(baskets)):
                b = baskets[i]
                if b >= f:
                    found = True
                    baskets[i] = 0
                    break
            if not found:
                res += 1
        return res
        
