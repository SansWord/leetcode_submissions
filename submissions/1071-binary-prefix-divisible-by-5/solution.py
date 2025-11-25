class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = 0
        result = []
        for i in nums:
            curr *= 2
            curr += i
            result.append(curr % 5 == 0)
        
        return result
        
