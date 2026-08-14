class Solution:

    def largestSquareArea(self, bottomLeft, topRight):
        max_area = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i + 1, n):

                left = max(bottomLeft[i][0], bottomLeft[j][0])
                bottom = max(bottomLeft[i][1], bottomLeft[j][1])

                right = min(topRight[i][0], topRight[j][0])
                top = min(topRight[i][1], topRight[j][1])

                width = right - left
                height = top - bottom

                side = min(width, height)

                if side > 0:
                    area = side * side

                    if area > max_area:
                        max_area = area

        return max_area