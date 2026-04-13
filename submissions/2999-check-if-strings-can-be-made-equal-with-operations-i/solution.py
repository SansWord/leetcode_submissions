class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        (s1[0] + s1[2]) == (s2[0] + s2[2])

        firstS1 = s1[0] + s1[2]
        secondS1 = s1[1] + s1[3]

        return (
            (firstS1 == (s2[0] + s2[2]) or firstS1 == (s2[2] + s2[0])) 
            and 
            (secondS1 == (s2[1] + s2[3]) or secondS1 == (s2[3] + s2[1]))
        )
