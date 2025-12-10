class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        # simulation to get answer
        ans = 0
        queue = deque([[i, t] for i, t in enumerate(tickets)])
        while queue:
            id, t = queue.popleft()
            if t == 0:
                continue
            else:
                ans += 1
                t -= 1
                if id == k and t == 0:
                    return ans

                queue.append([id, t])
        """
        ans = 0
        req = tickets[k]

        # everyone in front of k and k would buy at most req tickets
        for t in range(k + 1):
            ans += min(req, tickets[t])

        # everyone after k would buy at most req-1 tickets
        for t in range(k+1, len(tickets)):
            ans += min(req-1, tickets[t])

        return ans

