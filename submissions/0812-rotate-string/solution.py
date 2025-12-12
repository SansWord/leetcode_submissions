class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            if self.checkString(s, goal, i):
                return True
        return False
    def checkString(self, s: str, goal: str, start: int) -> bool:
        LEN = len(s)
        for i in range(LEN):
            j = (i + start) % LEN
            if s[i] != goal[j]:
                return False
        return True
        
