class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        filterNum = 0

        for v in nums:
            filterNum ^= v
                
        return filterNum
        
        
