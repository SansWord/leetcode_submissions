class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        preSet = set()
        postOccurrence = defaultdict(int)
        resultSet = set()

        for c in s:
            postOccurrence[c] += 1

        for m in s:
            postOccurrence[m] -= 1

            for c in preSet:
                if postOccurrence[c] > 0:
                    resultSet.add(c + m)

            preSet.add(m)


        return len(resultSet)

        
