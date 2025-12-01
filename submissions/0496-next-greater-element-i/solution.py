class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_to_idx = {}
        res = [-1] * len(nums1)
        for i, n in enumerate(nums1):
            num1_to_idx[n] = i
        stack = []

        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                smaller = stack.pop()
                res[num1_to_idx[smaller]] = num
            if num in num1_to_idx:
                stack.append(num)
        return res


        
