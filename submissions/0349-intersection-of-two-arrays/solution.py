class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            needles, hay = nums1, nums2
        else:
            hay, needles = nums1, nums2
        
        haySet = set(hay)
        res = set()
        for num in needles:
            if num in haySet:
                res.add(num)
        return list(res)
        
