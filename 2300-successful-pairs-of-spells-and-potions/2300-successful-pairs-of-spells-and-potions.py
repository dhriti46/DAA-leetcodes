class Solution:

    def successfulPairs(self, spells, potions, success):

        potions.sort()

        answer = []

        for spell in spells:

            low = 0
            high = len(potions)

            while low < high:

                mid = (low + high) // 2

                if spell * potions[mid] >= success:
                    high = mid
                else:
                    low = mid + 1

            answer.append(len(potions) - low)

        return answer