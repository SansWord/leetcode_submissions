class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        if k == 26:
            return 1

        # compress s so that a character can repeat at most 3 times
        # 3 times because that means no matter which one is being replaced, the effect is still the same
        compressedS = []
        pre = None
        count = 0
        for c in s:
            if c != pre:
                compressedS.append(c)
                pre = c
                count = 1
            else:
                count += 1
                if count <= 3:
                    compressedS.append(c)
        
        s = "".join(compressedS)

        replacementChoice = set()
        chars = []
        for c in s:
            replacementChoice.add(c)
            chars.append(c)

        if len(replacementChoice) != 26:
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c not in replacementChoice:
                    replacementChoice.add(c)
                    break

        
        LEN = len(chars)

        def findKEnd(chars:list[str], start: int) -> int:
            end = len(chars)
            pre = None
            distinct = set()
            for i in range(start, end):
                subC = chars[i]
                if not subC in distinct:
                    if len(distinct) == k:
                        return i-1
                    else:
                        distinct.add(subC)
            return end-1

        def generatePartitions(chars:list[str]):
            partition_starts = []
            LEN = len(chars)
            l = 0
            while l <= LEN - 1:
                partition_starts.append(l)
                rangeEnd = findKEnd(chars, l)
                l = rangeEnd + 1
            partitions = [None for i in range(LEN)]

            partitionsCount = len(partition_starts)
            for i in range(partitionsCount):
                start = partition_starts[i]
                if i+1 < partitionsCount:
                    end = partition_starts[i+1]
                else:
                    end = LEN
                for j in range(start, end):
                    partitions[j] = (start, end-1, i+1)
            return partitions

        partitions = generatePartitions(chars)
        reversed_partitions = generatePartitions(chars[::-1])
        suff = [ partition[2] for partition in reversed_partitions[::-1] ]

        # when replacement, choice be one of the shown character, or a nother one not in the set.
        operationMax = 0
        for i in range(LEN):
            #print("=== replacement at i:", i)
            originC = chars[i]
            # find r
            p_start = partitions[i][0]
            
            for c in replacementChoice:
                chars[i] = c

                r1 = findKEnd(chars, p_start)
                
                # r1 determined
                if r1 >= i:
                
                    if r1 + 1 >= LEN:
                        suffCount = 0
                    else:
                        suffCount = suff[r1+1]

                    if p_start - 1 < 0:
                        prefCount = 0
                    else:
                        prefCount = partitions[p_start - 1][2]
                    operations = 1 + prefCount + suffCount
                    #print(operations, i, c, r1)

                else:
                    # r1 < i, find r2
                    r2 = findKEnd(chars, r1+1)
                    if p_start - 1 < 0:
                        prefCount = 0
                    else:
                        prefCount = partitions[p_start - 1][2]

                    if r2 + 1 >= LEN:
                        suffCount = 0
                    else:
                        suffCount = suff[r2+1]
                    operations = prefCount + 2 + suffCount
                    #print(operations, i, c, r1, r2)                


                operationMax = max(operations, operationMax)


            chars[i] = originC
        
        return operationMax

