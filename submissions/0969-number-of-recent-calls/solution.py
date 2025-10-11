class RecentCounter:

    def __init__(self):
        self.requests = deque()
        

    def ping(self, t: int) -> int:
        while self.requests:
            if t - self.requests[0] > 3000:
                self.requests.popleft()
            else:
                break

        self.requests.append(t)
        return len(self.requests)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
