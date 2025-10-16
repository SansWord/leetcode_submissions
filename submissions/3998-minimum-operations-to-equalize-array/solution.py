class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pre = nums[0]
        for num in nums:
            if num != pre:
                return 1
        return 0
        
