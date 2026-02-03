class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # step means the nth times the number changes order, so when step is even, we expect to be increasing
        # and if step is odd, we expect to be decreasing
        # otheriwse, it flips again and step is increased by 1

        # make sure the first phrase is increasing, otherwise it's not trionic
        if nums[0] >= nums[1]:
            return False
        
        step = 0

        # checks from the third element with the second element as previous number
        pre = nums[1]
        for n in nums[2:]:

            # we're expecting strict increasing/decreasing, hence returns False if we got the same number
            if n == pre:
                return False
            
            # decide if we're expecting increasing or decreasing in the current step
            if step % 2 == 0:
                comp = lambda a, b: a < b
            else:
                comp = lambda a, b: a > b

            # if the comparator does not meet, means we're flipping and move to next step
            if not comp(pre, n):
                step += 1
                    
            # we're expecting 2 steps for a trionic array, so if it's greater than 2, returns False
            if step > 2:
                return False

            pre = n
        
        # we're expecting 2 steps for a trionic array
        return step == 2

        
