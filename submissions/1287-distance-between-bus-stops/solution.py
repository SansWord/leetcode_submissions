class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        LEN = len(distance)
        self.distance = distance
        
        if start < destination:
            small, big = start, destination
        else:
            small, big = destination, start
        
        clockwiseSum = self.calculateDistanceBetweenNodes(small, big)
        counterClockwiseSum = self.calculateDistanceBetweenNodes(big, LEN-1) + self.calculateDistanceBetweenNodes(0, small) + self.distance[LEN-1]

        return min(clockwiseSum, counterClockwiseSum)

        
    # 0 <= start <= destination < N
    def calculateDistanceBetweenNodes(self, start: int, destination: int) -> int:
        totalDistance = 0
        for i in range(start, destination):
            totalDistance += self.distance[i]
        return totalDistance
    
        
        
