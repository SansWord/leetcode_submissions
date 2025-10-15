class Solution:
    def longestPalindrome(self, s: str) -> str:
        LEN = len(s)
        pLens = [ [False for i in range(LEN)] for i in range(LEN)]
        
        # [i,i] is True
        # [i,i+1] is True if [i] == [i]
        # [l, k] is True if [l+1, k-1] is True and [l] == [k]
        maxLen = 1
        maxL = 0
        maxR = 0

        # carefully iterate over matrix by the distance to the diagonal points
        # e.g. for a 4x4 matrix, order should be
        # 0,0 1,1 2,2 3,3 (diagonal)
        # 0,1 1,2 2,3     (distance = 1)
        # 0,2 1,3         (distance = 2)
        # 0,3             (distance = 3)

        for i in range(LEN):
            for l in range(0, LEN-i):
                r = l + i

                isPalindrome = False

                if l == r:
                    isPalindrome = True
                elif s[l] == s[r]:
                    if r == l+1:
                        isPalindrome = True
                    elif pLens[l+1][r-1]:
                        isPalindrome = True
                
                if isPalindrome:
                    pLens[l][r] = True
                    currLen = r-l + 1
                    if currLen > maxLen:
                        maxLen = currLen
                        maxL = l
                        maxR = r

        return s[maxL:maxR+1]
