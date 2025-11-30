class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        counts = {
            0: 0,
            1: 0,
            2: 0
        }
        for num in nums:
            counts[num] += 1
        curr_idx = 0
        for i in range(counts[0]):
            nums[curr_idx] = 0
            curr_idx += 1
        for i in range(counts[1]):
            nums[curr_idx] = 1
            curr_idx += 1
        for i in range(counts[2]):
            nums[curr_idx] = 2
            curr_idx += 1

        
