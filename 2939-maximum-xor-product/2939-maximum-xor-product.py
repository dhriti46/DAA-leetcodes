class Solution:

    def maximumXorProduct(self, a, b, n):

        mod = 1000000007

        ax = (a >> n) << n
        bx = (b >> n) << n

        for i in range(n - 1, -1, -1):

            x = (a >> i) & 1
            y = (b >> i) & 1

            if x == y:
                ax = ax | (1 << i)
                bx = bx | (1 << i)

            elif ax < bx:
                ax = ax | (1 << i)

            else:
                bx = bx | (1 << i)

        return (ax * bx) % mod