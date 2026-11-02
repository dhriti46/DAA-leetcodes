class Solution(object):
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda x: x[0] - x[1])

        n = len(costs) // 2
        total = 0

        for i in range(len(costs)):
            if i < n:
                total += costs[i][0]
            else:
                total += costs[i][1]

        return total      