class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        number = n
        for i in range(n):
            number ^= i
            number ^= nums[i]
        
        return number
        
