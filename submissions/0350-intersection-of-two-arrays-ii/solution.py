class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fq1 = defaultdict(int)
        fq2 = defaultdict(int)
        for num in nums1:
            fq1[num] += 1
        for num in nums2:
            fq2[num] += 1
        
        res = []
        for v in fq1.keys():
            if v in fq2:
                fq = min(fq1[v], fq2[v])
                for i in range(fq):
                    res.append(v)

        return res
        
