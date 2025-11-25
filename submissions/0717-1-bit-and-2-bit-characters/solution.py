class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        result = []

        # a represent two-digit, b represent one-digit
        mid = False
        for bit in bits:
            if mid:
                mid = False
                result.append("a")
            else:
                if bit == 1:
                    mid = True
                else:
                    result.append("b")
        
        return result[-1] == "b"
        

        
