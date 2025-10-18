class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        i = 0
        while i < len(nums):
            num = nums[i]
            idx = num - 1
            if nums[idx] != num:
                print(nums[i], nums[idx])
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
        res = []
        for i in range(len(nums)):
            num = nums[i]
            if i+1 != num:
                res.append(i+1)

        return res
            
        
