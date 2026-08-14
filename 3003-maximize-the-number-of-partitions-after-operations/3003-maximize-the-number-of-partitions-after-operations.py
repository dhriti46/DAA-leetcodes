class Solution:

    def maxPartitionsAfterOperations(self, s, k):

        n = len(s)

        dp = {(0, 0): 0}

        answer = 0

        for ch in s:

            bit = 1 << (ord(ch) - ord('a'))
            new_dp = {}

            for (mask, changed), parts in dp.items():

                new_mask = mask | bit

                if bin(new_mask).count("1") <= k:
                    key = (new_mask, changed)
                    new_dp[key] = max(new_dp.get(key, -1), parts)
                else:
                    key = (bit, changed)
                    new_dp[key] = max(new_dp.get(key, -1), parts + 1)

                if changed == 0:

                    for c in range(26):

                        new_bit = 1 << c
                        changed_mask = mask | new_bit

                        if bin(changed_mask).count("1") <= k:
                            key = (changed_mask, 1)
                            new_dp[key] = max(new_dp.get(key, -1), parts)
                        else:
                            key = (new_bit, 1)
                            new_dp[key] = max(new_dp.get(key, -1), parts + 1)

            dp = new_dp

        for (mask, changed), parts in dp.items():
            answer = max(answer, parts + 1)

        return answer