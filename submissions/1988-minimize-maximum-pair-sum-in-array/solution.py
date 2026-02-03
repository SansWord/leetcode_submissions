class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        LEN = len(nums)
        nums.sort()
        result = float("-inf")
        for i in range(LEN//2):
            left = nums[i]
            right = nums[LEN-i-1]
            result = max(result, left + right)
        return result

        
