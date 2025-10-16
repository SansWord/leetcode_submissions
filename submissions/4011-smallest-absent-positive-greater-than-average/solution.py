class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums)/len(nums)
        if avg > 0:
            lowerBound = floor(sum(nums)/len(nums)) + 1
        else:
            lowerBound = 1
        
        greaters = set()
        for num in nums:
            if num >= lowerBound:
                greaters.add(num)
        
        while True:
            if not lowerBound in greaters:
                return lowerBound
            lowerBound += 1
