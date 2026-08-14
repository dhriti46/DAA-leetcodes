class Solution:

    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        if xCenter < x1:
            x = x1
        elif xCenter > x2:
            x = x2
        else:
            x = xCenter

        if yCenter < y1:
            y = y1
        elif yCenter > y2:
            y = y2
        else:
            y = yCenter

        distance = (x - xCenter) ** 2 + (y - yCenter) ** 2

        if distance <= radius ** 2:
            return True
        else:
            return False