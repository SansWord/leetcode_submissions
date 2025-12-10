class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = {0:0, 1:0}

        # counts requirements of students
        for i in students:
            counts[i] += 1

        # start serving sandwich, check if the served one is wanted by students
        for s in sandwiches:
            if counts[s] != 0:
                counts[s] -= 1
            else:
                return counts[0] + counts[1]

        return 0
