class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer–Moore variant
        elm1 = None
        elm1Count = 0
        elm2 = None
        elm2Count = 0

        for n in nums:
            if elm1 == n:
                elm1Count += 1
            elif elm2 == n:
                elm2Count += 1
            else:
                if elm1Count == 0:
                    elm1 = n
                    elm1Count = 1
                elif elm2Count == 0:
                    elm2 = n
                    elm2Count = 1
                else:    
                    elm1Count -= 1
                    elm2Count -= 1
        
        feq = {}
        if elm1Count != 0:
            feq[elm1] = 0
        if elm2Count != 0:
            feq[elm2] = 0

        for n in nums:
            if n in feq:
                feq[n] += 1
        
        result = []
        for k,v in feq.items():
            if v > len(nums)//3:
                result.append(k)

        return result
        

        
