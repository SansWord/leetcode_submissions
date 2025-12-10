class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        LEN = len(arr)
        zeros = 0
        for n in arr:
            if n == 0:
                zeros += 1
        
        i = LEN - 1
        j = LEN - 1 + zeros

        while i != j:
            if j < LEN:
                arr[j] = arr[i]
            j -= 1
            
            if arr[i] == 0:
                if j < LEN:
                    arr[j] = arr[i]
                j -= 1

            i -= 1

