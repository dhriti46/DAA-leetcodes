class Solution(object):
    def findSubstringInWraproundString(self, s):
        count = [0] * 26
        current = 0

        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                current += 1
            else:
                current = 1

            index = ord(s[i]) - ord('a')
            count[index] = max(count[index], current)

        return sum(count)