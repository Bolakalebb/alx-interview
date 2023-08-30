#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    """
    change = 0
    index = 0
    # sort coins in descending order
    coins.sort(reverse=True)
    while total > 0:
        if index >= len(coins):
            return -1
        if coins[index] <= total:
            total -= coins[index]
            change += 1
        else:
            index += 1
    return change
