class Solution:

    def canMakePaliQueries(self, s, queries):

        n = len(s)

        prefix = [[0] * 26 for i in range(n + 1)]

        for i in range(n):
            prefix[i + 1] = list(prefix[i])

            index = ord(s[i]) - ord('a')
            prefix[i + 1][index] += 1

        answer = []

        for left, right, k in queries:

            odd = 0

            for j in range(26):
                count = prefix[right + 1][j] - prefix[left][j]

                if count % 2 == 1:
                    odd += 1

            if odd // 2 <= k:
                answer.append(True)
            else:
                answer.append(False)

        return answer