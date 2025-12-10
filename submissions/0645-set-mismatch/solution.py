class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            if n < 0:
                curr = -n
            else:
                curr = n
            
            idx = curr - 1
            if nums[idx] < 0:
                res.append(curr)
            else:
                nums[idx] = - nums[idx]

        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)


        return res
        
