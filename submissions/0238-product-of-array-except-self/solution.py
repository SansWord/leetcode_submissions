class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        zeroCounts = 0
        allProduct = 1
        for num in nums:
            if num == 0:
                zeroCounts += 1
            else:
                allProduct *= num
        
        if zeroCounts > 1:
            return [ 0 ] * LEN
        elif zeroCounts == 1:
            return [ (0 if num != 0 else allProduct) for num in nums ]
        else:
            return [ allProduct//num for num in nums ]
