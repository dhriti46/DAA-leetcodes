class Solution:

    def countPathsWithXorValue(self, grid, k):

        m = len(grid)
        n = len(grid[0])
        MOD = 1000000007

        dp = [[[0] * 16 for j in range(n)] for i in range(m)]

        dp[0][0][grid[0][0]] = 1

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                value = grid[i][j]

                if i > 0:
                    for x in range(16):
                        new_xor = x ^ value
                        dp[i][j][new_xor] += dp[i - 1][j][x]
                        dp[i][j][new_xor] %= MOD

                if j > 0:
                    for x in range(16):
                        new_xor = x ^ value
                        dp[i][j][new_xor] += dp[i][j - 1][x]
                        dp[i][j][new_xor] %= MOD

        return dp[m - 1][n - 1][k]