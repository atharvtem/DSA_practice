import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for x, y in points:
            dist = round(((x)**2 + (y)**2),2)
            arr.append(dist)
        map = {i:[] for i in arr}
        for i in range(len(arr)):
            map[arr[i]].append(points[i])
        heapq.heapify(arr)
        res = []
        while k>0:
            temp = heapq.heappop(arr)
            k-=1
            res.append(map[temp].pop())

        return res