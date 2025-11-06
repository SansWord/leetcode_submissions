class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 1. using connections to construct partitions with find-union
        # 2. for a query [1,x], identify its partition, check if x is online or not and returns the smallest:
        #    using heap to track smallest station, pop if the smallest one is offline
        # time complexity: connection for for O(log(n) * num of C)
        #                  query: O(1) to identify partition and amorites O(1) to get smallest: O(1) for each query
        #                  O(num fo query)
        # space complexity: O(n): for union, partition-heap and aliveness bool array

        self.parents = [ i for i in range(c+1) ]
        
        for p1, p2 in connections:
            self.union(p1, p2)
        
        # aliveness track for each p to be alive or not
        aliveness = [True for i in range(c+1)]

        # partitions is heap of each partition so we can returns the smallest alive p
        partitions = {}

        for p in range(c+1):
            root = self.find(p)
            if root not in partitions:
                partitions[root] = []
            heapq.heappush(partitions[root], p)

        # now aliveness and partitions are constructed
        result = []
        for q, p in queries:
            match q:
                case 1:
                    if aliveness[p]:
                        result.append(p)
                    else:
                        found = False
                        partition = partitions[self.find(p)]
                        while partition:
                            if aliveness[partition[0]]:
                                result.append(partition[0])
                                found = True
                                break
                            else:
                                heapq.heappop(partition)
                        if not found:
                            result.append(-1)
                case 2:
                    aliveness[p] = False

        return result
        
        
    
    def find(self, child: int) -> int:
        if self.parents[child] != child:
            self.parents[child] = self.find(self.parents[child])
        return self.parents[child]

    def union(self, node1: int, node2) -> bool:
        p1 = self.find(node1)
        p2 = self.find(node2)
        self.parents[p1] = p2

