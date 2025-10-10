class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        rowNumber = 0
        for c in columnTitle:
            rowNumber *= 26

            # this means Z, the 25th symbol is treated as 26
            # we have an add 1 implicitly
            rowNumber += (ord(c) - 64) 
        
        return rowNumber
        
