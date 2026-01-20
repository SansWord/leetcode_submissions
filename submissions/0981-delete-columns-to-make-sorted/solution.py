class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        for j in range(len(strs[0])):
            pre_ord = float("-inf")
            for i in range(len(strs)):
                curr_ord = ord(strs[i][j])
                if pre_ord > curr_ord:
                    result += 1
                    break
                else:
                    pre_ord = curr_ord

        return result
        
