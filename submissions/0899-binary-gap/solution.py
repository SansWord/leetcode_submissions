class Solution:
    def binaryGap(self, n: int) -> int:
        maxGap = 0
        pre1 = -1
        level = 0
        while n != 0:
            if n%2 == 1:
                if pre1 == -1:
                    pre1 = level
                else:
                    gap = level - pre1
                    if gap > maxGap:
                        maxGap = gap
                    pre1 = level

            level += 1
            n //= 2

        return maxGap
        
