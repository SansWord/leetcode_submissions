class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # setup union-find
        self.parent = [ i for i in range(len(edges)+1) ]
        self.rank = [ 0 for i in range(len(edges)+1) ]

        for v1, v2 in edges:
            if not self.union(v1, v2):
                return [v1, v2]
    
    def union(self, v1: int, v2: int) -> bool:
        v1P = self.find(v1)
        v2P = self.find(v2)
        if v1P == v2P:
            return False
        rankV1P = self.rank[v1P]
        rankV2P = self.rank[v2P]

        if rankV1P == rankV2P:
            self.rank[v2P] = rankV2P + 1
            self.parent[v1P] = v2P
        elif rankV1P < rankV2P:
            self.parent[v1P] = v2P
        else:
            self.parent[v2P] = v1P
        
        return True
    
    def find(self, v: int) -> int:
        if not self.parent[v] == v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
        
