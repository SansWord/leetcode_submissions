class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        maxLen = 0
        occur = set()
        for r in range(len(s)):
            c = s[r]
            while c in occur:
                occur.remove(s[l])
                l += 1
            occur.add(c)
            currLen = r-l + 1
            maxLen = maxLen if maxLen >= currLen else currLen

        return maxLen

