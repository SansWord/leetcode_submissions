class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]
        for move in moves:
            match move:
                case "U":
                    pos[1] += 1
                case "D":
                    pos[1] -= 1
                case "R":
                    pos[0] += 1
                case "L":
                    pos[0] -= 1
        return pos[0] == 0 and pos[1] == 0



        
