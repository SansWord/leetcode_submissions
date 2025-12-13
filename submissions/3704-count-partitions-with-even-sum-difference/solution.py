class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        if not totalSum % 2 == 0:
            return 0
        else:
            return len(nums) - 1
        
