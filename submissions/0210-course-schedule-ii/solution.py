class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        for pair in prerequisites:
            c, req = pair
            edges[req].append(c)

        self.stack = []
        self.edges = edges
        self.visited = [False] * numCourses
        self.numCourses = numCourses
        
        for i in range(numCourses):
            if not self.visited[i]:
                if self.walk(i):
                    return []

        result = self.stack[::-1]
        courseIdxs = {}

        for idx, course in enumerate(result):
            courseIdxs[course] = idx
        
        for course, nextCourse in edges.items():
            courseIdx = courseIdxs[course]
            for nC in nextCourse:
                nCIdx = courseIdxs[nC]
                if nCIdx < courseIdx:
                    return []

        return result
    def walk(self, course: int) -> bool:
        self.visited[course] = True
        courses = self.edges[course]
        for c in courses:
            if not self.visited[c]:
                self.walk(c)
        self.stack.append(course)
        return False

        
