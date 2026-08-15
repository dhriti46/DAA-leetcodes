class Solution:

    def maxProfitAssignment(self, difficulty, profit, worker):

        jobs = []

        for i in range(len(difficulty)):
            jobs.append([difficulty[i], profit[i]])

        jobs.sort()

        worker.sort()

        answer = 0
        best = 0
        j = 0

        for ability in worker:

            while j < len(jobs) and jobs[j][0] <= ability:
                best = max(best, jobs[j][1])
                j += 1

            answer += best

        return answer