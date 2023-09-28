from math import inf
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = list(zip(quality, wage))
        workers_sorted = sorted(workers, key=lambda x: x[0]/x[1])
        heap = []

        least_quality_sum = [0 for i in range(n)]
        least_quality_sum[n - 1] = workers_sorted[n-1][0]
        heapq.heappush(heap, -workers_sorted[n-1][0])

        for i in range(n-2, -1, -1):
            heapq.heappush(heap, -workers_sorted[i][0])
            least_quality_sum[i] = least_quality_sum[i+1] + workers_sorted[i][0]
            j = 0
            if len(heap) > k:
                j = heapq.heappop(heap)     
            least_quality_sum[i] = least_quality_sum[i] + j

        min_cost = inf

        for i, x in enumerate(workers_sorted):
            if i > n - k:
                break
            cost = x[1] * (least_quality_sum[i]/x[0])
            if cost < min_cost:
                min_cost = cost

        return min_cost




