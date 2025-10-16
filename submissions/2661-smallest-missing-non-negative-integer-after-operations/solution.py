class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # found mod value for each nums
        mods = [0 for i in range(value) ]

        for num in nums:
            mods[num%value] += 1
        
        # find smallest count in mods
        minCount = float("inf")
        minMod = None
        for i in range(value):
            count = mods[i]
            if count < minCount:
                minCount = count
                minMod = i
        return minCount * value + minMod
        

        
