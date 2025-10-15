class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # lo, hi are inclusive

        def partition(lo, hi):


            # randomly select 3 values close middle, pick the middle one as pivot
            # doing this to avoid some testcases that predict picking strategy and make it a worst case.
            mid = (lo+hi) // 2
            p1Idx = mid
            p1 = nums[p1Idx]
            p2Idx = min(mid + p1%3, hi)
            p2 = nums[p2Idx]
            p3Idx = max(mid - p2 % 3, lo)
            p3 = nums[p3Idx]

            if p1 >= p2:
                if p2 >= p3:
                    pivot = p2
                    pIdx = p2Idx
                elif p1 >= p3:
                    pivot = p3
                    pIdx = p3Idx
                else:
                    pivot = p1
                    pIdx = p1Idx
            elif p1 >= p3:
                pivot = p1
                pIdx = p1Idx
            elif p2 <= p3:
                pivot = p2
                pIdx = p2Idx
            else:
                pivot = p3
                pIdx = p3Idx


            nums[pIdx], nums[lo] = nums[lo], nums[pIdx]
            pivot = nums[lo]
            left = lo
            right = hi
            i = lo
            while i <= right:
                n = nums[i]
                if n < pivot:
                    nums[left], nums[i] = n, nums[left]
                    left+= 1
                    i += 1
                elif n > pivot:
                    nums[right], nums[i] = n, nums[right]
                    right -= 1
                else:
                    i += 1
            return left-1, right+1
        

        def quick_sort(lo, hi):
            if lo >= hi:
                return
            pivotLeft, pivotRight = partition(lo, hi)

            # sort the shorter side to avoid deep recursion level
            if pivotLeft - lo < hi - pivotRight:
                quick_sort(lo, pivotLeft)
                quick_sort(pivotRight, hi)
            else:
                quick_sort(pivotRight, hi)
                quick_sort(lo, pivotLeft)
                
                    


        quick_sort(0, len(nums)-1)
        return nums
