class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select
    
        # l, r are inclusive
        def quick_select(l, r, targetKth) -> int:
            pLeft, pRight = partition(l, r)
            rightCounts = r - pRight
            
            if rightCounts >= targetKth:
                return quick_select(pRight + 1, r, targetKth)
            else:
                targetKth -= rightCounts
                sameCount = pRight - pLeft + 1
                if sameCount >= targetKth:
                    return nums[pRight]
                else:
                    targetKth -= sameCount
                    return quick_select(l, pLeft - 1, targetKth)
                
                

        # l, r are inclusive
        def partition(l, r) -> tuple[int, int]:
            if l == r:
                return l,r

            pIdx = randint(l, r)
            nums[pIdx], nums[l] = nums[l], nums[pIdx]

            pivot = nums[l]

            lt = l
            gt = r
            i = l

            # for i in range(l, r):
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            return lt, gt

        
        return quick_select(0, len(nums)-1, k)
        
