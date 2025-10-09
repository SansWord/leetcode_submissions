class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimumLength = min([len(s) for s in strs])
        if minimumLength == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        for i in range(minimumLength):
            prefixes = [s[i] for s in strs]
            # if prefixes are not all identitcal
            if len(set(prefixes)) != 1:
                return strs[0][:i]

        return strs[0][:minimumLength]
        
