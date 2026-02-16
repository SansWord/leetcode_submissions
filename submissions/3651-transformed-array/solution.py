class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        result = [0] * LEN
        for i in range(LEN):
            result[i] = nums[(nums[i]+i)%LEN]
        
        return result
        
