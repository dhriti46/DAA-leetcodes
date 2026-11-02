class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1]
        indices = [0] * len(primes)

        for _ in range(1, n):
            next_num = float('inf')

            for i in range(len(primes)):
                next_num = min(next_num, primes[i] * ugly[indices[i]])

            ugly.append(next_num)

            for i in range(len(primes)):
                if primes[i] * ugly[indices[i]] == next_num:
                    indices[i] += 1

        return ugly[-1]