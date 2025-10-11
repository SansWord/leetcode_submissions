class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        [cell1, cell2] = s.split(":")
        result = []
        col1 = ord(cell1[0])
        row1 = int(cell1[1])
        col2 = ord(cell2[0])
        row2 = int(cell2[1])
        
        
        for c in range(col1, col2+1):
            for r in range(row1, row2+1):
                result.append(f"{chr(c)}{r}")

        return result
