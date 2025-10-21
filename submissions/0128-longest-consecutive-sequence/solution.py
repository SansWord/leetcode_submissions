class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        maxSeqLen = 0
        for num in numSet:
            if not (num - 1) in numSet:
                curr = num
                currLen = 1
                while curr + 1 in numSet:
                    currLen += 1
                    curr += 1
                maxSeqLen = max(maxSeqLen, currLen)
        
        return maxSeqLen

