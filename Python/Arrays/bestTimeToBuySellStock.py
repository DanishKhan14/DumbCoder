"""
Max profit that we can get in a day is determined by the minimum prices in previous days.
For example, if we have prices array [3,2,5,8,1] we can calculate the min prices array [3,2,2,2,1]
and get the difference in our max profit array [0,0,3,6,0]. We can see clearly the max profit is 6,
which is buy from the index 1 and sell in index 3.
"""

def maxProfit(prices):
    min_seen, max_profit = float('inf'), 0
    for p in prices:
        min_seen = min(min_seen, p)
        curr_profit = p - min_seen
        max_profit = max(curr_profit, max_profit)
    return max_profit


