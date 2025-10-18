class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == "0":
            return num2
        
        if num2 == "0":
            return num1

        # num1 and num2 are not "0"

        charToInt = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        intToChar = "0123456789"

        num1Len = len(num1)
        num2Len = len(num2)

        carry = 0
        idx1 = 1
        idx2 = 1
        res = []

        while idx1 <= num1Len and idx2 <= num2Len:
            char1 = num1[num1Len - idx1]
            char2 = num2[num2Len - idx2]
            digit1 = charToInt[char1]
            digit2 = charToInt[char2]
            
            curSum = digit1 + digit2 + carry
            digit = curSum % 10
            carry = curSum // 10
            res.append(intToChar[digit])

            idx1 += 1
            idx2 += 1
        
        restIdx = None
        restNum = None

        if idx1 <= num1Len:
            restIdx = idx1
            restNum = num1
            restLen = num1Len
        
        if idx2 <= num2Len:
            restIdx = idx2
            restNum = num2
            restLen = num2Len
        
        if restNum:
            while restIdx <= restLen:
                char = restNum[restLen - restIdx]
                digit = charToInt[char]
                
                curSum = digit + carry
                digit = curSum % 10
                carry = curSum // 10
                res.append(intToChar[digit])

                restIdx += 1
        
        if carry != 0:
            res.append(intToChar[carry])

        return "".join(res[::-1])
