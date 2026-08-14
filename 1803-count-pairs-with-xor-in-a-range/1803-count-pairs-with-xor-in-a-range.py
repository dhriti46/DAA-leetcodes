class Solution:

    def countPairs(self, nums, low, high):

        class Node:
            def __init__(self):
                self.child = [None, None]
                self.count = 0

        root = Node()

        def insert(num):
            node = root

            for bit in range(15, -1, -1):
                b = (num >> bit) & 1

                if node.child[b] is None:
                    node.child[b] = Node()

                node = node.child[b]
                node.count += 1

        def countLessEqual(num, limit):
            node = root
            result = 0

            for bit in range(15, -1, -1):

                if node is None:
                    break

                b = (num >> bit) & 1
                lb = (limit >> bit) & 1

                if lb == 1:
                    if node.child[b] is not None:
                        result += node.child[b].count

                    node = node.child[1 - b]

                else:
                    node = node.child[b]

            if node is not None:
                result += node.count

            return result

        answer = 0

        for num in nums:
            answer += countLessEqual(num, high)
            answer -= countLessEqual(num, low - 1)

            insert(num)

        return answer