class Solution(object):
    def predictPartyVictory(self, senate):
        radiant = []
        dire = []
        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.pop(0)
            d = dire.pop(0)

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"