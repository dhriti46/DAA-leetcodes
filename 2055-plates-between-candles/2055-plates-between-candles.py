class Solution:

    def platesBetweenCandles(self, s, queries):

        n = len(s)

        prefix = [0] * (n + 1)
        left_candle = [-1] * n
        right_candle = [-1] * n

        count = 0

        for i in range(n):
            if s[i] == '*':
                count += 1

            prefix[i + 1] = count

        last = -1

        for i in range(n):
            if s[i] == '|':
                last = i

            left_candle[i] = last

        last = -1

        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                last = i

            right_candle[i] = last

        answer = []

        for left, right in queries:

            first = right_candle[left]
            last = left_candle[right]

            if first == -1 or last == -1 or first >= last:
                answer.append(0)
            else:
                plates = prefix[last] - prefix[first + 1]
                answer.append(plates)

        return answer