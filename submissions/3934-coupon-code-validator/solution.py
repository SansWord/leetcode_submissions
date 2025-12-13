class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        categories = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        validCodes = [
            [],
            [],
            [],
            []
        ]
        
        for i in range(len(code)):
            currCode = code[i]
            currCategory = businessLine[i]
            if (isActive[i] and currCategory in ["electronics", "grocery", "pharmacy", "restaurant"] 
            and self.isValid(currCode)):
                validCodes[categories[currCategory]].append(currCode)
        
        sortedValidCodes = [ sorted(sublist) for sublist in validCodes ]
        
        return [code for sublist in sortedValidCodes for code in sublist]

    def isValid(self, code:str) -> bool:
        if len(code) > 0:
            for c in code.lower():
                if not c in "abcdefghijklmnopqrstuvwxyz_0123456789":
                    return False
            return True
        else:
            return False
        
