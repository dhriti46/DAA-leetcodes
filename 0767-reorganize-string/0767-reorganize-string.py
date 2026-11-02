import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        freq = Counter(s)

        if max(freq.values()) > (len(s) + 1) // 2:
            return ""

        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)

        result = []

        while len(heap) > 1:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)

            result.append(char1)
            result.append(char2)

            if count1 + 1 < 0:
                heapq.heappush(heap, (count1 + 1, char1))

            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, char2))

        if heap:
            result.append(heapq.heappop(heap)[1])

        return ''.join(result)