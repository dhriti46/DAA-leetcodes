class Solution:

    def findMaximumXOR(self, nums):

        answer = 0
        mask = 0

        for i in range(30, -1, -1):

            mask = mask | (1 << i)

            prefixes = set()

            for num in nums:
                prefixes.add(num & mask)

            candidate = answer | (1 << i)

            for prefix in prefixes:

                if (prefix ^ candidate) in prefixes:
                    answer = candidate
                    break

        return answer