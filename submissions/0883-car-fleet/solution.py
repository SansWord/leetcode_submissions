class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)

        stack = []
        for car in cars:
            position, speed = car
            eta = (target-position)/speed
            if not stack or stack[-1] < eta:
                stack.append(eta)

        return len(stack)
        
