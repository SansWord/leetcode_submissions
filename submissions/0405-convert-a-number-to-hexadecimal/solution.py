class Solution:
    def toHex(self, num: int) -> str:
        hexChr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

        if num == 0:
            return "0"
        
        isNegative = num < 0
        if isNegative:
            num = -(num+1)

        res = []
        for i in range(8):
            idx = num%16

            if isNegative:
                idx = 15 - idx                

            res.append(hexChr[idx])
            num //= 16

            if not isNegative and num == 0:
                break

        return "".join(res[::-1])
        
        
