class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lo = 0
        hi = len(nums) - 1
        result = []

        while lo <= hi:
            if abs(nums[lo]) <= abs(nums[hi]):
                result.append(nums[hi]**2)
                hi -= 1
            else:
                result.append(nums[lo]**2)
                lo += 1

        return result[::-1]
        
