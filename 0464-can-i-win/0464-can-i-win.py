class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal <= 0:
            return True

        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if total < desiredTotal:
            return False

        memo = {}

        def can_win(used, remaining):
            if used in memo:
                return memo[used]

            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << i

                if not (used & bit):
                    if i >= remaining or not can_win(used | bit, remaining - i):
                        memo[used] = True
                        return True

            memo[used] = False
            return False

        return can_win(0, desiredTotal)     