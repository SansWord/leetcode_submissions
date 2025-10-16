class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        LEN = len(nums)

        incParStart = -1
        for i in range(LEN-1, 0, -1):
            if nums[i] > nums[i-1]:
                incParStart = i-1
                break
        
        if incParStart == -1:
            rev(0, LEN-1)
            return
        
        # sort incParStart+1 to end of list
        # but since incParStart is the last increasing pair
        # incParStart+1 to end must be decreasing
        # hence just revse
        rev(incParStart+1, LEN-1)

        # find the first number after incParStart that is greater than key
        # swap those two numbers
        # the number must exists because incParStart+1 (the second element of the pair) is there.
        # but that could be too big, we need the first number greater than pairStart
        key = nums[incParStart]
        for i in range(incParStart+1, LEN):
            if nums[i] > key:
                nums[incParStart], nums[i] = nums[i], key
                return

