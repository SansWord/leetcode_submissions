class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if stack:
                while stack and stack[-1][0] < t:
                    _, preIdx = stack.pop()
                    result[preIdx] = i - preIdx
            
            stack.append((t, i))

        return result
        
