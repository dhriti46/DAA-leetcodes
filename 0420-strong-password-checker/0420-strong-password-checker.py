class Solution:

    def strongPasswordChecker(self, password):

        n = len(password)

        lower = False
        upper = False
        digit = False

        for ch in password:
            if ch.islower():
                lower = True
            elif ch.isupper():
                upper = True
            elif ch.isdigit():
                digit = True

        missing = 0

        if not lower:
            missing += 1
        if not upper:
            missing += 1
        if not digit:
            missing += 1

        repeats = []

        i = 0

        while i < n:
            j = i

            while j < n and password[j] == password[i]:
                j += 1

            length = j - i

            if length >= 3:
                repeats.append(length)

            i = j

        # Password is too short
        if n < 6:
            return max(6 - n, missing)

        replacements = 0

        for length in repeats:
            replacements += length // 3

        # Password is between 6 and 20
        if n <= 20:
            return max(replacements, missing)

        # Password is too long
        deletions = n - 20

        # First, use deletions where they reduce replacements most efficiently
        for mod in [0, 1, 2]:

            for i in range(len(repeats)):

                if deletions == 0:
                    break

                if repeats[i] < 3:
                    continue

                if repeats[i] % 3 == mod:

                    remove = min(deletions, mod + 1)

                    repeats[i] -= remove
                    deletions -= remove

        # Use remaining deletions: every 3 deletions reduce 1 replacement
        replacements = 0

        for length in repeats:
            replacements += length // 3

        replacements -= min(replacements, deletions // 3)

        deletions = n - 20

        return (n - 20) + max(replacements, missing)