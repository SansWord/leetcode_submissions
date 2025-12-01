class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        return self.RLE(self.countAndSay(n-1))

    def RLE(self, digitStr: str) -> str:
        pre = None
        count = 0
        res = ""
        for n in digitStr:
            if n == pre:
                count += 1
            else:
                if pre != None:
                    res += str(count)
                    res += str(pre)
                pre = n
                count = 1
        if pre != None:
            res += str(count)
            res += str(pre)
        
        return res


        
