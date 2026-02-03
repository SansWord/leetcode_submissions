class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
      # construct graph with edges and reversed edges
      graph = [ [] for _ in range(n) ]
      for d, s, c in edges:
        graph[d].append((s, c))
        graph[s].append((d, c*2))
      
      dist = [float("inf")] * n
      visited = [False] * n
      
      dist[0] = 0

      heap = []

      heapq.heappush(heap, (0,0))

      while heap:
        d, u = heapq.heappop(heap)
        if u == n-1:
          return d
        
        if visited[u]: continue

        visited[u] = True
        
        for v, weight in graph[u]:
          if dist[v] > dist[u] + weight:
            dist[v] = dist[u] + weight
            heapq.heappush(heap, (dist[v], v))

      return -1
        
