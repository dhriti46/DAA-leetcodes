class Solution:

    def maximumStrongPairXor(self, nums):

        nums.sort()

        trie = {}
        left = 0
        answer = 0

        def insert(num):

            node = trie

            for i in range(20, -1, -1):

                bit = (num >> i) & 1

                if bit not in node:
                    node[bit] = [0, {}]

                node[bit][0] += 1
                node = node[bit][1]

        def remove(num):

            node = trie

            for i in range(20, -1, -1):

                bit = (num >> i) & 1

                node[bit][0] -= 1
                node = node[bit][1]

        def findMax(num):

            node = trie
            result = 0

            for i in range(20, -1, -1):

                bit = (num >> i) & 1
                other = 1 - bit

                if other in node and node[other][0] > 0:
                    result = result | (1 << i)
                    node = node[other][1]
                else:
                    node = node[bit][1]

            return result

        for right in range(len(nums)):

            while nums[left] * 2 < nums[right]:
                remove(nums[left])
                left += 1

            insert(nums[right])

            answer = max(answer, findMax(nums[right]))

        return answer