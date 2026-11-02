
class Solution(object):
    def strWithout3a3b(self, a, b):
        result = []

        while a > 0 or b > 0:
            if a > b:
                if a > 0:
                    result.append('a')
                    a -= 1
                if a > b and a > 0:
                    result.append('a')
                    a -= 1
                if b > 0:
                    result.append('b')
                    b -= 1
            else:
                if b > 0:
                    result.append('b')
                    b -= 1
                if b > a and b > 0:
                    result.append('b')
                    b -= 1
                if a > 0:
                    result.append('a')
                    a -= 1

        return ''.join(result)