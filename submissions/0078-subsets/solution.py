class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[], nums]

        res = []
        rest = self.subsets(nums[1:])
        for sub_subset in rest:
            res.append([nums[0]] + sub_subset)
            res.append(sub_subset)
            
        return res
        
