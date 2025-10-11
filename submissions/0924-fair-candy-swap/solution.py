class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)



        fairNum = (aliceSum + bobSum) // 2

        aliceTake = aliceSum < fairNum

        diffNum = abs(aliceSum - fairNum)

        aliceSet = set(aliceSizes)
        bobSet = set(bobSizes)

        # find box from alice and bob with different number of d

        for aNum in aliceSet:
            bobTarget = aNum + diffNum * (1 if aliceTake else -1)

            if bobTarget in bobSet:
                return [aNum, bobTarget]
            
        
