class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        LEN = len(s)
        numArr = [int(c) for c in s]

        if a == 0:
            addingTimes = 1
        else:
            addingTimes = 10 // gcd(10, a)

        rotatingStrings = []
        
        if b % 2 == 0:
            # only odd indexes will be adding
            evenAddingTimes = 1
        else:
            # odd and even will be addingB
            evenAddingTimes = addingTimes
        
        # consider b is odd or even
        # if even, only odd-position will be alter
        for i in range(evenAddingTimes):
            evenAddedArr = numArr.copy()
            for evenIdx in range(0, LEN, 2):
                evenAddedArr[evenIdx] = (evenAddedArr[evenIdx] + i * a) % 10

            for j in range(addingTimes):
                oddAddedArr = evenAddedArr.copy()
                for oddIdx in range(1, LEN, 2):
                    oddAddedArr[oddIdx] = (oddAddedArr[oddIdx] + j * a) % 10
                
                rotatingStrings.append("".join([str(num) for num in oddAddedArr]) * 2)
                


        # consider len of s, and possible ways to roate string without repeat

        if b == 0:
            rotateTimes = 1
        else:
            rotateTimes = LEN // gcd(LEN, b)

        minRes = int(s)
        minStr = s
        alreadyRotated = set()
        for rotatingdStr in rotatingStrings:
            if rotatingdStr in alreadyRotated:
                continue
            else:
                alreadyRotated.add(rotatingdStr)
                for i in range(rotateTimes):
                    start = (i * b) % LEN
                    rotatedStr = rotatingdStr[start:start+LEN]
                    rotatedVal = int(rotatedStr)
                    if rotatedVal < minRes:
                        minRes = rotatedVal
                        minStr = rotatedStr
        
        return minStr


        



        
