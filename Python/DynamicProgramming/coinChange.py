#!/usr/bin/python
"""
Coin Change Problem
"""

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Method 1

        rs = [amount+1] * (amount+1)
        rs[0] = 0
        for i in xrange(1, amount+1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)

        if rs[amount] == amount+1:
            return -1
        return rs[amount]

        # Method 2:

        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in xrange(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]

        # Method 3: BFS

        level = seen = {0}
        number = 0
        while level:
            if amount in level:
                return number
            level = {a+c for a in level for c in coins if a+c <= amount} - seen
            seen |= level
            number += 1
        return -1