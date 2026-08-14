class Solution:
    def maximumLengthSubstring(self, s):
        count = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            ch = s[right]

            if ch not in count:
                count[ch] = 0

            count[ch] += 1

            while count[ch] > 2:
                count[s[left]] -= 1
                left += 1

            length = right - left + 1

            if length > max_length:
                max_length = length

        return max_length