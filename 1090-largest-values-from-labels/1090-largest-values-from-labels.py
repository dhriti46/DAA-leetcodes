
class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        items = sorted(zip(values, labels), reverse=True)

        count = {}
        total = 0
        selected = 0

        for value, label in items:
            if selected == numWanted:
                break

            if count.get(label, 0) < useLimit:
                total += value
                count[label] = count.get(label, 0) + 1
                selected += 1

        return total