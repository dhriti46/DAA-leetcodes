class Solution:

    def findCoins(self, numWays):

        n = len(numWays)

        dp = [0] * (n + 1)
        dp[0] = 1

        answer = []

        for coin in range(1, n + 1):

            if dp[coin] > numWays[coin - 1]:
                return []

            if dp[coin] < numWays[coin - 1]:

                if dp[coin] + 1 != numWays[coin - 1]:
                    return []

                answer.append(coin)

                for amount in range(coin, n + 1):
                    dp[amount] += dp[amount - coin]

        if dp[1:] != numWays:
            return []

        return answer