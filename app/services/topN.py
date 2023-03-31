from typing import List
import heapq

class topNService():
    @staticmethod
    def search_top_n(arr: List[int], n: int) -> List[int]:
        heap = []
        for i in arr:
            heapq.heappush(heap, i)
            if len(heap) > n:
                heapq.heappop(heap)
        res = [0] * n
        for i in range(n-1, -1, -1):
            res[i] = heapq.heappop(heap)
        return res
