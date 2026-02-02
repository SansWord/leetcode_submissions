class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # minimum 3 sum, including first element of given array
        # find the least 2 elements of this array excluding the first element
        first = float("inf")
        second = float("inf")

        for n in nums[1:]:
            if n < first:
                third = second
                second = first
                first = n
            elif n < second:
                third = second
                second = n
        
        return first + second + nums[0]
        
