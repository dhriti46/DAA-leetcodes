class Solution:

    def maximizeXor(self, nums, queries):

        nums.sort()

        queries2 = []

        for i in range(len(queries)):
            queries2.append([queries[i][0], queries[i][1], i])

        queries2.sort(key=lambda x: x[1])

        trie = {}
        answer = [-1] * len(queries)

        index = 0

        for x, m, q in queries2:

            while index < len(nums) and nums[index] <= m:

                num = nums[index]
                node = trie

                for bit in range(30, -1, -1):

                    b = (num >> bit) & 1

                    if b not in node:
                        node[b] = {}

                    node = node[b]

                index += 1

            if not trie:
                answer[q] = -1
                continue

            node = trie
            value = 0

            for bit in range(30, -1, -1):

                b = (x >> bit) & 1
                opposite = 1 - b

                if opposite in node:
                    value = value | (1 << bit)
                    node = node[opposite]
                else:
                    node = node[b]

            answer[q] = value

        return answer