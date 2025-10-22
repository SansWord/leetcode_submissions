import heapq

def search_shortest_paths(nodes: int, edges: list[tuple[int, int, int]], start: int) -> list[int]:

	adjacents = [[] for i in range(nodes)]
	for edge in edges:
		v1, v2, weight = edge
		adjacents[v1].append((v2, weight))
		adjacents[v2].append((v1, weight))
	visited = [False] * nodes
	distances = [-1] * nodes
	pre = [-1] * nodes

	distances[start] = 0
	visited[start] = True

	q = []
	heapq.heappush(q, (0, start))
	while q:
		curr_dis, curr = heapq.heappop(q)
		visited[curr] = True
		if curr_dis > distances[curr]:
			continue
		for adj, weight in adjacents[curr]:
			if visited[adj]:
				continue
			adj_dis = curr_dis + weight
			if distances[adj] == -1 or distances[adj] > adj_dis:
				distances[adj] = adj_dis
				pre[adj] = curr
				heapq.heappush(q, (adj_dis, adj))
			else:
				print(f"== saw node:{adj}, skip")
		print(distances, pre, q)


	return distances



def main() -> None:
	edges = [
		(0,1,2),
		(0,2,8),
		(1,2,5),
		(1,3,6),
		(2,3,3),
		(2,4,2),
		(3,4,1),
		(3,5,9),
		(4,5,3)
	]
	print(search_shortest_paths(6, edges, 0))

if __name__ == '__main__':
	main()