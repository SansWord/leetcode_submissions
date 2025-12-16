class Solution:
    def makeFancyString(self, s: str) -> str:
        pre = None
        count = 0
        result = []
        for c in s:
            if c != pre:
                count = 1
                pre = c
                result.append(c)
            else:
                if count < 2:
                    count += 1
                    result.append(c)

        return "".join(result)
                    
        
