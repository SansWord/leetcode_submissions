class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        pre = float("-inf")
        for num in nums:
            if num > pre:
                pre = num
            else:
                new_vale = pre + 1
                res += new_vale - num
                pre = new_vale

        return res
        
        
