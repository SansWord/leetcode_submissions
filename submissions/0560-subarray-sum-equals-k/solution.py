class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCounts = defaultdict(int)
        # indicate no prefix
        prefixSumCounts[0] = 1
        total = 0
        counts = 0
        for num in nums:
            total += num
            counts += prefixSumCounts[total-k]
            prefixSumCounts[total] += 1
        
        return counts

        
