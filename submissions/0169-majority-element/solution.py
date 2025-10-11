class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore alogrithm because n had majority
        count = 0
        maxElm = None

        for n in nums:
            if count == 0:
                maxElm = n
                count = 1
            else:
                if n == maxElm:
                    count += 1
                else:
                    count -= 1


        return maxElm
        
