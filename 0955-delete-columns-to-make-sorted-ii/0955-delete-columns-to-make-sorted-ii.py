class Solution(object):
    def minDeletionSize(self, strs):
        rows = len(strs)
        cols = len(strs[0])
        deleted = 0
        sorted_pairs = [False] * (rows - 1)

        for c in range(cols):
            valid = True

            for r in range(rows - 1):
                if not sorted_pairs[r] and strs[r][c] > strs[r + 1][c]:
                    valid = False
                    break

            if not valid:
                deleted += 1
                continue

            for r in range(rows - 1):
                if strs[r][c] < strs[r + 1][c]:
                    sorted_pairs[r] = True

        return deleted