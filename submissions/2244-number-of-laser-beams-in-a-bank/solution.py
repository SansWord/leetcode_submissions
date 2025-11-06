class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        pre = 0
        for row in bank:
            curr = 0
            for c in row:
                if c == "1":
                    curr += 1
            if curr == 0:
                continue
            total += pre * curr
            pre = curr
        return total
        
