from math import gcd
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        LENGTH = len(nums)
        if LENGTH <= 1:
            return

        # concider list with n elements and k rotation
        # breaks n into groups, each has length of n / gcd(n, k).
        # circular swapping theses groups

        k = k % LENGTH
        order = self.calculate_cycle_order(LENGTH, k)
        num_group = LENGTH // order

        for i in range(num_group):
            tmp = nums[i]
            curr = i
            for j in range(order-1):
                nextIdx = (curr - k) % LENGTH
                nums[curr] = nums[nextIdx]
                curr = nextIdx
            nums[i+k] = tmp
        

            
    def calculate_cycle_order(self, n: int, k: int) -> int:
        # calculate gcd and then return n/gcd
        return n // gcd(n, k)


        



        
