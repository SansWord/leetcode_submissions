class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = float("inf")
        pairs = []
        for i in range(len(arr)-1):
            a = arr[i]
            b = arr[i+1]
            curr_diff = b - a
            if curr_diff < diff:
                diff = curr_diff
                pairs = [[a, b]]
            elif curr_diff == diff:
                pairs.append([a, b])
        return pairs
