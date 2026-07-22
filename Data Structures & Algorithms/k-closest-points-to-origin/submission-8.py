import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for i, p in enumerate(points):
            distances.append([i, (math.sqrt(((0 - p[0])**2) + ((0 - p[1])**2)))])

        distances.sort(key=lambda x: x[1])

        answer = []
        for i in range(k):
            answer.append(distances[i][0])

        return [points[i] for i in answer]