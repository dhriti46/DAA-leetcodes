from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            if count[card] > 0:
                freq = count[card]

                for i in range(card, card + groupSize):
                    if count[i] < freq:
                        return False

                    count[i] -= freq

        return True      