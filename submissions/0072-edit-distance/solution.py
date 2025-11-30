class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        LEN1 = len(word1)
        LEN2 = len(word2)
        
        dist = [ [float("inf")] * (LEN2 + 1) for _ in range(LEN1 + 1) ]
        dist[-1][-1] = 0
        for i in range(LEN2):
            dist[-1][i] = LEN2 - i
        for i in range(LEN1):
            dist[i][-1] = LEN1 - i

        for i in range(LEN1-1, -1, -1):
            for j in range(LEN2-1, -1, -1):
                if word1[i] == word2[j]:
                    dist[i][j] = dist[i+1][j+1]
                else:
                    dist[i][j] = 1 + min(dist[i+1][j+1], dist[i][j+1], dist[i+1][j])

        return dist[0][0]

        
