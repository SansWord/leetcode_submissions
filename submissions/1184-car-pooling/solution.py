class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengerDelta = defaultdict(int)
        minDist = float("inf")
        maxDist = -1
        for trip in trips:
            numPassengers, start, end = trip
            minDist = min(minDist, start)
            maxDist = max(maxDist, end)
            passengerDelta[start] += numPassengers
            passengerDelta[end] -= numPassengers
        
        print(passengerDelta)

        occupied = 0
        for dist in range(minDist, maxDist + 1):
            delta = passengerDelta[dist]
            occupied += delta
            if occupied > capacity:
                return False

        return True
            
        
