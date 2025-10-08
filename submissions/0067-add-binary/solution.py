class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""

        if len(a) < len(b):
            small = a
            big = b
        else:
            small = b
            big = a
        

        len_small = len(small)
        len_big = len(big)

        carry = "0"
        for i in range(len_small):
            idx = -(i+1)
            digit_small = small[idx]
            digit_big = big[idx]
            # print(idx, digit_small, digit_big, carry, result)

            if digit_small == digit_big:
                result += carry
                if digit_small == "1":
                    carry = "1"
                else:
                    carry = "0"
            else:
                if carry == "0":
                    result += "1"
                else:
                    result += "0"
                    carry = "1"

        # print(carry, result)

        for i in range(len_small, len_big):
            idx = -(i+1)
            digit_big = big[idx]
            # print(idx, digit_big, carry)

            if carry == "0":
                result += digit_big
            else:
                if digit_big == "1":
                    carry = "1"
                    result += "0"
                else:
                    carry = "0"
                    result += "1"
        
        if carry == "1":
            result += "1"

        return result[::-1]
