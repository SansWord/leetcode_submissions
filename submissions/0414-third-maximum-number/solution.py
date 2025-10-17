class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        firstMax = float("-inf")
        secondMax = float("-inf")
        thirdMax = float("-inf")
        for num in nums:
            # tracking k max
            if num > thirdMax:
                if num > firstMax:
                    thirdMax = secondMax
                    secondMax = firstMax
                    firstMax = num
                elif num > secondMax and num < firstMax:
                    thirdMax = secondMax
                    secondMax = num
                elif num < secondMax:
                    thirdMax = num
            
        if thirdMax > float("-inf"):
            return thirdMax
        else:
            return firstMax
        
