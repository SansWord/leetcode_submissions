class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # n, k = (n-1)*2-1
        # 0       6    2 <---- str[  0] + " "*(n-2) + str[k+  0]
        # 1     5 7  1 3 <---- str[  1] + " "*(n-3) + str[k+  1] 
        # 2    4  8 0  4 <---- str[  2] + " "*(n-3) + str[k+  2] 
        # 3       9    5 <---- str[  3] + " "*(n-3) + str[k+  3] 
        # .
        # .
        # n-3  n+1   9    5 <---- str[n-1] + " " + s + " "*(n-2 - 2) + str[k+n-1]
        # n-2 n    9    5 <---- str[n-1] + s + " "*(n-2 - 1) + str[k+n-1]
        # n-1     9    5 <---- str[n-1] + " "*(n-2) + str[k+n-1]

        if numRows == 1:
            return s

        string_length = len(s)
        k = numRows - 1 + numRows - 2 + 1

        result = ""

        # first row
        for i in range(0, string_length, k):
            result += s[i]

        # second to n-1th row, which has one extra character
        for r in range(1, numRows - 1):
            for i in range(r, string_length, k):
                result += s[i]
                next_idx = i + k - r*2
                if next_idx < string_length:
                    result += s[next_idx]
        
        # last row
        for i in range(numRows - 1, string_length, k):
            result += s[i]
        
        return result
