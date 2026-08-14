class Solution:

    def maxAbsValExpr(self, arr1, arr2):
        max_value = 0

        for s1 in [1, -1]:
            for s2 in [1, -1]:

                maximum = -float('inf')
                minimum = float('inf')

                for i in range(len(arr1)):
                    value = s1 * arr1[i] + s2 * arr2[i] + i

                    maximum = max(maximum, value)
                    minimum = min(minimum, value)

                result = maximum - minimum

                if result > max_value:
                    max_value = result

        return max_value