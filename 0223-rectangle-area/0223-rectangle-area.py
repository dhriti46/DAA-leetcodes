class Solution:

    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):

        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        left = max(ax1, bx1)
        right = min(ax2, bx2)

        bottom = max(ay1, by1)
        top = min(ay2, by2)

        overlap = 0

        if right > left and top > bottom:
            overlap = (right - left) * (top - bottom)

        return area1 + area2 - overlap