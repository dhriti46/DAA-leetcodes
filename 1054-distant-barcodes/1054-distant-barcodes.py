
import heapq
from collections import Counter

class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        freq = Counter(barcodes)
        heap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(heap)

        result = []

        while heap:
            count1, num1 = heapq.heappop(heap)
            result.append(num1)

            if heap:
                count2, num2 = heapq.heappop(heap)
                result.append(num2)

                count2 += 1
                if count2 < 0:
                    heapq.heappush(heap, (count2, num2))

            count1 += 1
            if count1 < 0:
                heapq.heappush(heap, (count1, num1))

        return result