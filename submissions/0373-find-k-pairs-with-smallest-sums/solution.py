class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        LEN1 = len(nums1)
        LEN2 = len(nums2)

        # put the first point into heap
        visited = {(0,0)}
        q = [(nums1[0]+nums2[0], (0, 0))]

        found = 0
        res = []
        
        while found < k and q:

            total, idxes = heapq.heappop(q)
            x, y = idxes
            res.append([nums1[x], nums2[y]])
            found += 1

            # for the given smallest pair, the next possible smallest will be next to it.
            # add both points into q
            nextPoints = [(x+1, y), (x, y+1)]
            for p in nextPoints:
                if not p in visited:
                    new_x, new_y = p

                    # boundry check for new point
                    if new_x >= 0 and new_x < LEN1 and new_y >= 0 and new_y < LEN2:
                        visited.add(p)
                        n1 = nums1[new_x]
                        n2 = nums2[new_y]
                        heapq.heappush(q, (n1+n2, p))

        return res
        
