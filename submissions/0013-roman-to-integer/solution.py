class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        idx = 0
        sum = 0

        while idx < len(s):
            if idx == (len(s) - 1):
                sum += roman_to_int[s[idx]]
                break
            
            r = s[idx:idx+2]
            if r in roman_to_int:
                sum += roman_to_int[r]
                idx += 2
            else:
                r = s[idx]
                sum += roman_to_int[r]
                idx += 1

        return sum
        
