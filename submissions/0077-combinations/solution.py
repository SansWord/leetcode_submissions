class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combine_helper(tuple(i+1 for i in range(n)), k)

    @cache
    def combine_helper(self, nums: tuple[int, ...], k: int) -> list[list[int]]:
        if len(nums) == 0:
            return []
        if k == 0:
            return [[]]

        if k == 1:
            return [ [i] for i in nums ]
        
        if k == len(nums):
            return [ list(nums) ]
        
        if k >= len(nums):
            return []
        
        res = []
        for i in range(len(nums)-1):
            rest = self.combine_helper(nums[i+1:], k-1)
            if len(rest) == 0:
                break
            for com in rest:
                res.append([nums[i]] + com)
        
        return res

        
        
