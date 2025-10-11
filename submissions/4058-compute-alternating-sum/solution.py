class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        modifier = 1
        result = 0
        for n in nums:
            result += n * modifier
            modifier *= -1
        
        return result
        
