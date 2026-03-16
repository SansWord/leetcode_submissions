class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        totalCandies = len(candyType)
        types = set()
        for t in candyType:
            types.add(t)
        totalTypes = len(types)
        return min(totalCandies//2, totalTypes)
        
