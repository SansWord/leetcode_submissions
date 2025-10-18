class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = x ^ y
        return distance.bit_count()

        # if distance == 0:
        #     return 0
        # else:
        #     bits = 0
        #     while distance > 0:
        #         if distance % 2 == 1:
        #             bits += 1
        #         distance //= 2
        #     return bits

        
