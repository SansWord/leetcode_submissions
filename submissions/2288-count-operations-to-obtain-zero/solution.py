class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        if num1 > num2:
            big, small = num1, num2
        else:
            big, small = num2, num1

        while big != 0 and small != 0:
            count += big // small
            big, small = small, big % small
        
        return count
        
