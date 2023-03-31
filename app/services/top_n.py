import heapq


class TopNService:
    @staticmethod
    def search_top_n(arr: list[int], n: int) -> list[int]:
        heap = []
        for i in arr:
            heapq.heappush(heap, i)
            if len(heap) > n:
                heapq.heappop(heap)
        res = [0] * n
        for i in range(n - 1, -1, -1):
            res[i] = heapq.heappop(heap)
        return res
