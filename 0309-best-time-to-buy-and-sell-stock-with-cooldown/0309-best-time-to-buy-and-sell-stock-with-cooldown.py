class Solution(object):
    def maxProfit(self, prices):
        hold = float('-inf')
        sold = 0
        cooldown = 0

        for price in prices:
            prev_sold = sold

            sold = hold + price
            hold = max(hold, cooldown - price)
            cooldown = max(cooldown, prev_sold)

        return max(sold, cooldown) 