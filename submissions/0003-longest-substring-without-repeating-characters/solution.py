class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        start = False
        maxLength = 0
        startIdx = -1

        for i in range(len(s)):
            c = s[i]
            if not start:
                start = True
                startIdx = i
            else:
                if c in s[startIdx:i]:
                    for j in range(startIdx, i):
                        if s[j] == c:
                            startIdx = j+1
                            break
            
            currLength = i - startIdx + 1
            
            if currLength > maxLength:
                maxLength = currLength

        return maxLength

            


        
