class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        
        incomingEdges = [None] * (N + 1)
        candidateEdges = []
        for parent, child in edges:
            if incomingEdges[child]:
                candidateEdges.append(incomingEdges[child])
                candidateEdges.append([parent, child])
                break
            else:
                incomingEdges[child] = [parent, child]

        if not candidateEdges:
            # pure cycle detection
            return self.removeCycle(edges)
        else:
            # remove one of the edge and check cycle
            edge1 = candidateEdges[1]
            edge2 = candidateEdges[0]
            print(candidateEdges)
            if not self.removeCycle(edges, edge1):
                return edge1
            else:
                return edge2

    def removeCycle(self, edges: List[List[int]], removingEdge=None) -> list[int]:
        self.parent = [ i for i in range(len(edges) + 1) ]
        self.rank = [ 0 for i in range(len(edges) + 1) ]

        for edge in edges:
            if edge != removingEdge:
                if not self.union(edge):
                    return edge
        return None

    def union(self, edge: list[int]) -> bool:
        v1 = edge[0]
        v2 = edge[1]

        v1P = self.find(v1)
        v2P = self.find(v2)
        if v1P == v2P:
            return False
        
        rankV1P = self.rank[v1P]
        rankV2P = self.rank[v2P]

        if rankV1P == rankV2P:
            self.parent[v1P] =v2P
            self.rank[v2P] += 1
        elif rankV1P < rankV2P:
            self.parent[v1P] =v2P
        else:
            self.parent[v2P] =v1P

        return True
    
    def find(self, v: int) -> int:
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
        

    

        

        
