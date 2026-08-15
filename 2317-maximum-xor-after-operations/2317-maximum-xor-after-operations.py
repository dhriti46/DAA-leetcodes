class Solution:

    def maximumXOR(self, nums):

        basis = [0] * 31

        for num in nums:

            x = num

            for i in range(30, -1, -1):

                if (x >> i) & 1:

                    if basis[i] == 0:
                        basis[i] = x
                        break

                    x = x ^ basis[i]

        answer = 0

        for i in range(30, -1, -1):

            answer = max(answer, answer ^ basis[i])

        return answer