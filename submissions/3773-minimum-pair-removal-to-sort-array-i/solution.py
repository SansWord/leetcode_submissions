class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        while not self.isSorted(nums):
            nums = self.mergePair(nums)
            count += 1
        
        return count
    
    def mergePair(self, nums: List[int]) -> List[int]:
        idx = -1
        min_pair = float("inf")

        for i in range(len(nums)-1):
            curr_pair = nums[i] + nums[i+1]
            if curr_pair < min_pair:
                min_pair = curr_pair
                idx = i
        
        nums[idx] = nums[idx] + nums[idx+1]
        nums.pop(idx+1)

        return nums
    
    def isSorted(self, nums: List[int]) -> Bool:
        if len(nums) <= 1:
            return True
        
        curr = float("-inf")
        for num in nums:
            if num >= curr:
                curr = num
            else:
                return False
        return True
