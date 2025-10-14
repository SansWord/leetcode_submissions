class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        LEN = len(nums)

        increasing = [False] * LEN
        increasing[0] = True
        for i in range(1, LEN):
            if nums[i] > nums[i-1]:
                increasing[i] = True

        foundFirst = False
        increasingLen = 0
        decreasingLen = 0
        for i, inc in enumerate(increasing):

            if not inc:
                decreasingLen += 1

                if increasingLen >= k:
                    foundFirst = True
                else:
                    foundFirst = False
                
                if decreasingLen > 2:
                    foundFirst = False    
                increasingLen = 1
                
            else:
                increasingLen += 1
                decreasingLen = 1

            if increasingLen == 2*k:
                return True

            if foundFirst and increasingLen == k:
                return True
        
        return False
        
        



        
