class Solution(object):
    def matrixScore(self, grid):
        m = len(grid)
        n = len(grid[0])

        result = 0

        for c in range(n):
            ones = 0

            for r in range(m):
                if grid[r][0] == 0:
                    ones += 1 - grid[r][c]
                else:
                    ones += grid[r][c]

            ones = max(ones, m - ones)
            result += ones * (1 << (n - c - 1))

        return result