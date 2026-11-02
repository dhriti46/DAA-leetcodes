
class Solution(object):
    def rob(self, nums):
        def helper(arr):
            prev1 = 0
            prev2 = 0

            for num in arr:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr

            return prev1

        if len(nums) == 1:
            return nums[0]

        return max(helper(nums[:-1]), helper(nums[1:]))