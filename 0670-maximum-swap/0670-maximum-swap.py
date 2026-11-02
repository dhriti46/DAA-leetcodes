class Solution(object):
    def maximumSwap(self, num):
        digits = list(str(num))
        last = {}

        for i, digit in enumerate(digits):
            last[digit] = i

        for i, digit in enumerate(digits):
            for d in range(9, int(digit), -1):
                if str(d) in last and last[str(d)] > i:
                    j = last[str(d)]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))

        return num      