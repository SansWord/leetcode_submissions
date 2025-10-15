class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for pair in prerequisites:
            c, req = pair
            edges[req].append(c)
        visited = [False] * numCourses

        self.edges = edges
        self.visited = visited

        
        for i in range(numCourses):
            if not visited[i]:
                if not self.walk(i, []):
                    return False
        return True

    def walk(self, course:int, visiting: list[int]) -> bool:
        visiting.append(course)
        nextCourses = self.edges[course]
        for nextCourse in nextCourses:
            if nextCourse in visiting:
                return False
            if not self.visited[nextCourse]:
                if not self.walk(nextCourse, visiting):
                    return False
        visiting.pop()
        self.visited[course] = True
        return True


        
