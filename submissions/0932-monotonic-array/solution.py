class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True

        increasing = True
        decreasing = True

        for i in range(1, len(nums)):
            pre = nums[i-1]
            curr = nums[i]

            if pre < curr:
                decreasing = False
            
            if curr < pre:
                increasing = False

            if not decreasing and not increasing:
                return False
        
        return True
        
        
