#!/usr/bin/env python

# Time:  O(n^c)

class Solution:
    def __init__(self):
        self.memo = {}

    def minNumberOfCoins(self, amount, denominations):
        if amount == 0:
            return 0
       
        if amount in self.memo:
            return self.memo[amount]

        n = amount + 1
        for coin in denominations:
            curr = 0
            if amount >= coin:
                next = self.minNumberOfCoins(amount - coin, denominations)
                if next >= 0:
                    curr = 1 + next
            if curr > 0:
                n = min(n, curr)

        if n == amount + 1:
            return -1
        else:
            self.memo[amount] = n
            return n


if __name__ == '__main__':
    for i in xrange(1, 21):
        print(Solution().minNumberOfCoins(i, [1, 2, 5]))
