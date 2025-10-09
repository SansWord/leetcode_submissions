class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        keys_to_remove = []
        for i, v in enumerate(nums):
            if v == val:
                keys_to_remove.append(i)

        result = len(nums) - len(keys_to_remove)
        
        for k in keys_to_remove[::-1]:
            nums.pop(k)

        return result
        
