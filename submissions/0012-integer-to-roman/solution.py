class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        while num != 0:
            if num >= 1000:
                num -= 1000
                result += "M"
                continue
            
            if num >= 900:
                num -= 900
                result += "CM"
                continue
            
            if num >= 500:
                num -= 500
                result += "D"
                continue
            
            if num >= 400:
                num -= 400
                result += "CD"
                continue

            if num >= 100:
                num -= 100
                result += "C"
                continue
            
            if num >= 90:
                num -= 90
                result += "XC"
                continue
            
            if num >= 50:
                num -= 50
                result += "L"
                continue
            
            if num >= 40:
                num -= 40
                result += "XL"
                continue
            
            if num >= 10:
                num -= 10
                result += "X"
                continue
            
            if num >= 9:
                num -= 9
                result += "IX"
                continue
            
            if num >= 5:
                num -= 5
                result += "V"
                continue
            
            if num >= 4:
                num -= 4
                result += "IV"
                continue
            
            if num >= 1:
                num -= 1
                result += "I"
                continue
            
            
            


        return result
        
