class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        # top-k question
        return sorted(list(set(nums)))[-k:][::-1]
        
        
