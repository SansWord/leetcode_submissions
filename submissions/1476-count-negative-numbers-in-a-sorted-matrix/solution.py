class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # find the index of the last positive number of given row
        # TODO using binary search 
        def find_last_positive_idx(row, start, end):
            for i, n in enumerate(grid[row]):
                if n < 0:
                    return i - 1
            return end

            left = start - 1
            right = end + 1
            while right - left > 1:
                mid = left + (right - left) // 2
                if grid[row][mid] < 0:
                    right = mid
                else:
                    left = mid
            
            return left


        start = 0
        end = n - 1
        total = 0

        for i in range(m):
            last_positive_idx = find_last_positive_idx(i, start, end)
            total += n - last_positive_idx - 1
            end = last_positive_idx

        return total
