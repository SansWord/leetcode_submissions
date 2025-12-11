class Solution:
    def isPossible(self, target: List[int]) -> bool:
        h = []
        total_sum = sum(target)
        for num in target:
            heapq.heappush(h, -num)
        
        # while the biggest is greater than 1
        while -h[0] > 1:
            currMax = -heapq.heappop(h)
            currRest = total_sum - currMax

            # this is impossible state, hence can't be constructed
            if currRest == 0 or currMax - currRest < 1:
                return False
            
            
            # find preMax that is not the max anymore
            # logically, keep substracting currMax by currRest until it's smaller than currRest
            # but that is equal to modulor with zero check
            preMax = currMax % currRest
            if preMax == 0:
                preMax = currRest
            
            # put preMax into heap
            heapq.heappush(h, -preMax)

            # update total_sum
            total_sum -= currMax - preMax


        # exit while loop, means all elements are 1
        return True
        
