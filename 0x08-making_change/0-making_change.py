#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    ********************************************
    ****determine the fewest number of coins****
    *******needed to meet a given amount********
    ********************************************
    @coins: is a list of the values of the coins
            in the possession
    @total: given amount
    Return:
            fewest number of coins needed to meet total
            *** If total is 0 or less, return 0
            *** If total cannot be met by any number
                of coins you have, return -1
    """
    if (type(total) is not int or type(coins) is not list):
        return -1
    if total <= 0:
        return 0
    try:
        Min = [float('inf') for i in range(total+1)]
        Min[0] = 0
        for i in range(1, total+1):
            for j in range(len(coins)):
                if Min[i - coins[j]] + 1 < Min[i]:
                    Min[i] = Min[i - coins[j]] + 1

        if Min[total] != float('inf'):
            return Min[total]
        else:
            return -1
    except Exception:
        return -1
