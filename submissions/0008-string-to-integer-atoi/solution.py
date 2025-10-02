class Solution:
    def myAtoi(self, s: str) -> int:
        sum = 0
        start = False
        is_negative = False
        for c in s:
            if not start:
                if c == " ":
                    continue
                else:
                    start = True
                    # reading +-, digit or others
                    if c in "0123456789":
                        is_negative = False
                        sum += int(c)
                        continue
                    
                    if c in "+-":
                        is_negative = (c == "-") 
                        continue
                    # read other character
                    break
            else:
                if c in "0123456789":
                    sum *= 10
                    sum += int(c)
                    # rounding
                    if sum >= 2147483648:
                        if is_negative:
                            return -2147483648
                        else:
                            return 2147483647
                    continue
                
                # reading other character
                break
        
        if is_negative:
            sum *= -1

        return sum
            
        
