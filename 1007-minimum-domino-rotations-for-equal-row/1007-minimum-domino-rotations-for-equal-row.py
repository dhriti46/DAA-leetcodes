
class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        def check(target):
            rotate_top = 0
            rotate_bottom = 0

            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return -1

                if tops[i] != target:
                    rotate_top += 1

                if bottoms[i] != target:
                    rotate_bottom += 1

            return min(rotate_top, rotate_bottom)

        result = check(tops[0])

        if result != -1:
            return result

        return check(bottoms[0])      