from math import log
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0

        rounds = minutesToTest // minutesToDie

        pigs = 1
        while (rounds+1)**pigs < buckets:
            pigs += 1

        return pigs
