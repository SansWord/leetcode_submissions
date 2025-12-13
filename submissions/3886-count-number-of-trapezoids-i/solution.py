class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MAX = 10**9 + 7
        point_groups = defaultdict(int)
        for point in points:
            point_groups[point[1]] += 1

        res = 0
        edges = 0
        for group_count in point_groups.values():
            curr_edges = (group_count * (group_count - 1) // 2) % MAX
            res += edges * curr_edges % MAX
            edges += curr_edges % MAX

        return res % MAX

        
