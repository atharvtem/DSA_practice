class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        heap = [-n for n in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            fir = heapq.heappop(heap)
            sec = heapq.heappop(heap)
            if sec > fir:
                heapq.heappush(heap,fir-sec)
        heapq.heappush(heap,0)
        return abs(heap[0])