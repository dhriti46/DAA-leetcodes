class Solution:

    def minimizeXor(self, num1, num2):

        count = bin(num2).count("1")
        x = 0

        for i in range(30, -1, -1):

            if count > 0 and (num1 & (1 << i)) != 0:
                x = x | (1 << i)
                count -= 1

        for i in range(31):

            if count > 0 and (num1 & (1 << i)) == 0:
                x = x | (1 << i)
                count -= 1

        return x