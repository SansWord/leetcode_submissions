class Solution:
    def trap(self, height: List[int]) -> int:
        possible_hold = [0] * len(height)
        pre = 0
        preIdx = -1
        possible = False

        for i,h in enumerate(height):
            if h < pre:
                possible = True
                possible_hold[i] = pre - h
            elif h >= pre:
                possible = False
                pre = h
                preIdx = i

        if possible:
            reversed_height = height[preIdx:][::-1]
            pre = 0
            preIdx = -1
            possible = False

            # backward from end to prevIdx, which left heigt is bigger than right height
            for i,h in enumerate(reversed_height):
                possible_hold[-(i+1)] = 0
                if h < pre:
                    possible = True
                    possible_hold[-(i+1)] = pre - h
                elif h >= pre:
                    possible = False
                    pre = h
                    preIdx = i

        return sum(possible_hold)
        
