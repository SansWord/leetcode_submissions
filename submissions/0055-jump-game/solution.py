class Solution:
    def canJump(self, nums: List[int]) -> bool:
        LEN = len(nums)
        
        minReachable = LEN - 1
        for i in range(LEN-1, -1, -1):
            if i + nums[i] >= minReachable:
                minReachable = i
        
        return minReachable == 0

        
