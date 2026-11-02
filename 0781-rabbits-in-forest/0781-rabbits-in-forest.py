class Solution(object):
    def numRabbits(self, answers):
        count = {}
        result = 0

        for answer in answers:
            count[answer] = count.get(answer, 0) + 1

        for answer, freq in count.items():
            group_size = answer + 1
            groups = (freq + group_size - 1) // group_size
            result += groups * group_size

        return result      