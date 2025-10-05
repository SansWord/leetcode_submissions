class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length1 = len(nums1)
        length2 = len(nums2)
        totalLength = length1 + length2
        leftPartitionNum = int((totalLength +1)/2)

        if length1 <= length2:
            needles = nums1
            hay = nums2
            
        else:
            needles = nums2
            hay = nums1

        start = 0
        end = len(needles)

        needleLength = len(needles)
        hayLength = len(hay)
        
        # print("needles", needles, "hay", hay)
        while start <= end:
            needleLeftNum =  int((start + end)/2)
            hayLeftNum = leftPartitionNum - needleLeftNum

            leftNeedleMax = float("-inf") if needleLeftNum == 0 else needles[needleLeftNum-1]
            rightNeedleMin = float("inf") if needleLeftNum == needleLength else needles[needleLeftNum]

            leftHayMax = float("-inf") if hayLeftNum == 0 else hay[hayLeftNum-1]
            rightHayMin = float("inf") if hayLeftNum == hayLength else hay[hayLeftNum]

            if leftNeedleMax <= rightHayMin and leftHayMax <= rightNeedleMin:
                if totalLength % 2 == 1:
                    return max(leftNeedleMax, leftHayMax)
                else:
                    return (max(leftNeedleMax, leftHayMax) + min(rightHayMin, rightNeedleMin))/2
            else:
                if leftNeedleMax > rightHayMin:
                    # too right
                    end = needleLeftNum
                else:
                    # too left
                    start = needleLeftNum+1
                    continue
        

            

        
