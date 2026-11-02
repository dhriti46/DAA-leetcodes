class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row_max = [max(row) for row in grid]
        col_max = [max(grid[r][c] for r in range(len(grid)))
                   for c in range(len(grid[0]))]

        result = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                result += min(row_max[r], col_max[c]) - grid[r][c]

        return result       