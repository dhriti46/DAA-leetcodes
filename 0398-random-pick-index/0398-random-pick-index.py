import random

class Solution:

    def __init__(self, nums):
        self.data = {}

        for i in range(len(nums)):
            if nums[i] not in self.data:
                self.data[nums[i]] = []

            self.data[nums[i]].append(i)

    def pick(self, target):
        indexes = self.data[target]
        return random.choice(indexes)