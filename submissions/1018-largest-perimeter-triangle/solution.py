class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        LEN = len(nums)
        for i in range(LEN-3, -1, -1):
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
            if a + b > c:
                return a + b + c

        return 0
