class Solution(object):
    def maxChunksToSorted(self, arr):
        count = 0
        max_value = 0

        for i in range(len(arr)):
            max_value = max(max_value, arr[i])

            if max_value == i:
                count += 1

        return count        