class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = set()
        zeroCounts = 0
        for num in arr:
            nums.add(num)
            if num == 0:
                zeroCounts += 1
        
        if zeroCounts > 1:
            return True
        
        for num in arr:
            if num != 0 and num*2 in nums:
                return True
        
        return False
        
        
