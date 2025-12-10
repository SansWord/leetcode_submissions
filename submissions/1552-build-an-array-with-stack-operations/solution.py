class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        push = "Push"
        pop = "Pop"
        res = []
    
        curr = 0
        for num in target:
            for i in range(curr + 1, num):
                res.append(push)
                res.append(pop)
            res.append(push)
            curr = num
        return res
