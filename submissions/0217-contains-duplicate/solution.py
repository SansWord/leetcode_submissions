class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occurrence = set()
        for n in nums:
            if n in occurrence:
                return True
            else:
                occurrence.add(n)

        return False
        
