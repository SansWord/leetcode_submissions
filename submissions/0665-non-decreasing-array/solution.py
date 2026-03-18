class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        LEN = len(nums)
        if LEN <= 2:
            return True

        modified = False
        first = nums[0]
        second = nums[1]

        if second < first:
            modified = True
            first = second

                
        
        for n in nums[2:]:
            if n >= second:
                first = second
                second = n
            else:
                if modified:
                    # the list is still invalide after first modification
                    return False
                else:
                    # modify list to make it valid
                    # the candidate is the current number or the previous number

                    modified = True

                    if n >= first:
                        # consider n is greater or equal than first, but smaller than second
                        # changes second to n
                        second = n
                    # else: n is smaller than both first and second, changes it to second

        return True




        
