class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            if i % 3 != 0:
                result += 1
        return result
