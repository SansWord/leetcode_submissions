class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        LEN = len(nums)
        for i in range(LEN):
            if start + i < LEN:
                if nums[start+i] == target:
                    return i
            if start - i >= 0:
                if nums[start-i] == target:
                    return i
        
