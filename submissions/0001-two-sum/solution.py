class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_positions = {}
        for i, v in enumerate(nums):
            if (target - v) in num_positions:
                return [num_positions[target-v], i]
            
            num_positions[v] = i
        
        
