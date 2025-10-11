class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        i = 0
        while n > 0:
            digit = n % 10
            if digit != 0:
                result.append(digit * 10**i)

            i += 1
            n //= 10
        
        return result[::-1]
