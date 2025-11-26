class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        result = 1
        start = 2
        SQRT_NUM = sqrt(num)
        while start <= SQRT_NUM:
            if num % start == 0:
                result += start
                rest =  num // start
                if rest != start:
                    result += rest
            if result > num:
                return False
            start += 1

        return result == num
        
