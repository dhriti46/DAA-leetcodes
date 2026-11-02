class Solution(object):
    def leastInterval(self, tasks, n):
        counts = [0] * 26

        for task in tasks:
            counts[ord(task) - ord('A')] += 1

        counts.sort(reverse=True)

        max_count = counts[0]
        idle = (max_count - 1) * n

        for i in range(1, 26):
            idle -= min(max_count - 1, counts[i])

        return len(tasks) + max(0, idle)