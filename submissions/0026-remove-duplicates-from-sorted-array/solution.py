class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        keys_to_remove = []

        curr = None

        for i,v in enumerate(nums):
            if v != curr:
                curr = v
            else:
                keys_to_remove.append(i)

        for i in range(len(keys_to_remove)):
            nums.pop(keys_to_remove.pop())
        
        return len(nums) - len(keys_to_remove)
        
