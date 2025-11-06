class Solution:
    def totalMoney(self, n: int) -> int:
        # 0 + ... + n-1 = n(n-1) / 2
        weeks = n // 7
        left = n % 7

        return   (28 + (28 + (weeks-1)*7)) * weeks // 2 + ((1 + weeks) + (left + weeks)) * left // 2

        
        
