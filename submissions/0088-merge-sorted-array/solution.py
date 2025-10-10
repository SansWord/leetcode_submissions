class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        l1Idx = m-1
        l2Idx = n-1

        for i in range(m+n-1, -1, -1):
            if l2Idx <0:
                return

            pickL1 = None
            if l1Idx < 0:
                pickL1 = False
                val2 = nums2[l2Idx]
            else:
                val1 = nums1[l1Idx]
                val2 = nums2[l2Idx]

                if val1 >= val2:
                    pickL1 = True
                else:
                    pickL1 = False

            if pickL1:
                nums1[i] = val1
                l1Idx -= 1
            else:
                nums1[i] = val2
                l2Idx -= 1
        
