#!/usr/bin/python3
"""
This is the main file used for testing the makeChange function.
"""


def makeChange(coins, amount):
    """
    Calculates the number of coins of each type needed to make the change for
    the given amount. It iterates through the list of coins, deducting the
    maximum possible number of each coin from the amount. If it's not possible
    to make the change, it returns -1.
    """
    if amount < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        num = amount // coin
        amount -= num * coin
        count += num
    return count if amount == 0 else -1
