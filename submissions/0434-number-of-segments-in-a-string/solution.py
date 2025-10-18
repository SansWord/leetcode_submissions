class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        pre = " "
        for c in s:
            if c != " " and pre == " ":
                count += 1
            pre = c

        return count
        
