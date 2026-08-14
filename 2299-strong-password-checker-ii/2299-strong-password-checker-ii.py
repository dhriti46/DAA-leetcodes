class Solution:

    def strongPasswordCheckerII(self, password):

        if len(password) < 8:
            return False

        lower = False
        upper = False
        digit = False
        special = False

        special_chars = "!@#$%^&*()-+"

        for i in range(len(password)):

            ch = password[i]

            if ch.islower():
                lower = True

            if ch.isupper():
                upper = True

            if ch.isdigit():
                digit = True

            if ch in special_chars:
                special = True

            if i > 0 and password[i] == password[i - 1]:
                return False

        if lower and upper and digit and special:
            return True

        return False