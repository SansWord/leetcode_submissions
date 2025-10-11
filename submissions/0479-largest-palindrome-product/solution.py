class Solution:
    def largestPalindrome(self, n: int) -> int:

        lower = 10**(n-1)
        upper = 10**n - 1
        if n > 1:
            oddUpper = 10**(n-1) - 1
            oddLower = 10**(n-2)
        
        #print("== check even digits")
        for i in range(upper, lower-1, -1):
            s = str(i)
            targetStr = s + s[::-1]
            target = int(targetStr)
            j = upper
            #print("check:", target)
            while j*j > target:
                if target % j == 0:
                    multiplier = target // j
                    if  multiplier <= upper and multiplier >= lower:
                        #print(target, j, multiplier)
                        return target % 1337
                j -= 1

        #print("== check odd digits")
        if n == 1:
            for target in range(9, -1, -1):
                j = upper
                #print("check:", target)
                while j*j >= target:
                    #print("check j:", j, target)
                    if target % j == 0:
                        multiplier = target // j
                        if  multiplier <= upper and multiplier >= lower:
                            #print(target, j, multiplier)
                            return target % 1337
                    j -= 1
        else:
            for i in range(oddUpper, oddLower-1, -1):
                for j in range(9, -1, -1):
                    s = str(i)
                    targetStr = s + str(j) + s[::-1]
                    target = int(targetStr)
                    j = upper
                    #print("check:", target)
                    while j*j > target:
                        #print("check j:", j, n)
                        if target % j == 0:
                            multiplier = target // j
                            if  multiplier <= upper and multiplier >= lower:
                                #print(target, j, multiplier)
                                return target % 1337
                        j -= 1
        
        return -1
        
