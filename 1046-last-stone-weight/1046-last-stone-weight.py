class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for s in stones: 
            heapq.heappush(heap, -s)
        while len(heap)>=2: 
            x = -1*heapq.heappop(heap)
            y = -1*heapq.heappop(heap)
            if x-y>0: heapq.heappush(heap, -(x-y))
        return -heap[0] if heap else 0